import os
os.environ["SC2PATH"] = "starcraftstuff/StarCraftII/"

# SC2 API
import sc2
from sc2 import run_game, maps, Race, Difficulty,position,Result
from sc2.player import Bot, Computer
from sc2.constants import UnitTypeId

# Tools
import time
import random

# ML part
import numpy as np
import cv2  # from opencv-python


draw_dict = {

    # 枢纽
    UnitTypeId.NEXUS: [15, (0, 255, 0)],
    # 水晶
    UnitTypeId.PYLON: [3, (20, 235, 0)],
    # 气矿
    UnitTypeId.ASSIMILATOR: [2, (55, 200, 0)],
    # 探机
    UnitTypeId.PROBE: [1, (55, 200, 0)],
    # BG
    UnitTypeId.GATEWAY: [3, (200, 100, 0)],
    # BY
    UnitTypeId.CYBERNETICSCORE: [3, (150, 150, 0)],
    # vr
    UnitTypeId.ROBOTICSFACILITY: [5, (215, 155, 0)],
    # VS
    UnitTypeId.STARGATE: [5, (255, 0, 0)],
    # 虚空
    UnitTypeId.VOIDRAY: [3, (255, 100, 0)],
}

# End visualization
HEADLESS = False

# Save data

main_base_names = ["nexus", "commandcenter", "hatchery"]

class SentdeBot(sc2.BotAI):
    def __init__(self):
        self.ITERATIONS_PER_MINUTE = 165
        self.MAX_WORKERS = 66
        self.do_something_after = 0
        self.train_data = []

    def random_location_variance(self, enemy_start_location):
        x = enemy_start_location[0]
        y = enemy_start_location[1]

        x += ((random.randrange(-20, 20))/100) * enemy_start_location[0]
        y += ((random.randrange(-20, 20))/100) * enemy_start_location[1]

        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if x > self.game_info.map_size[0]:
            x = self.game_info.map_size[0]
        if y > self.game_info.map_size[1]:
            y = self.game_info.map_size[1]

        go_to = position.Point2(position.Pointlike((x,y)))
        return go_to

    async def on_step(self, iteration):
        self.iteration = iteration
        await self.distribute_workers()
        await self.build_workers()
        await self.build_pylons()
        await self.build_assimilators()
        await self.expand()
        await self.offensive_force_buildings()
        await self.build_offensive_force()

        await self.intel()
        # await self.scout()
        await self.attack()

    async def build_workers(self):
        if (len(self.units(UnitTypeId.NEXUS)) * 16) > len(self.units(UnitTypeId.PROBE)) and len(
                self.units(UnitTypeId.PROBE)) < self.MAX_WORKERS:
            for nexus in self.units(UnitTypeId.NEXUS).ready.noqueue:
                if self.can_afford(UnitTypeId.PROBE):
                    await self.do(nexus.train(UnitTypeId.PROBE))

    async def build_pylons(self):
        if self.supply_left < 5 and not self.already_pending(UnitTypeId.PYLON):
            nexuses = self.units(UnitTypeId.NEXUS).ready
            if nexuses.exists:
                if self.can_afford(UnitTypeId.PYLON):
                    await self.build(UnitTypeId.PYLON, near=nexuses.first)

    async def build_assimilators(self):
        for nexus in self.units(UnitTypeId.NEXUS).ready:
            vaspenes = self.state.vespene_geyser.closer_than(15.0, nexus)
            for vaspene in vaspenes:
                if not self.can_afford(UnitTypeId.ASSIMILATOR):
                    break
                worker = self.select_build_worker(vaspene.position)
                if worker is None:
                    break
                if not self.units(UnitTypeId.ASSIMILATOR).closer_than(1.0, vaspene).exists:
                    await self.do(worker.build(UnitTypeId.ASSIMILATOR, vaspene))

    async def expand(self):
        if self.units(UnitTypeId.NEXUS).amount < (self.iteration / self.ITERATIONS_PER_MINUTE) and self.units(UnitTypeId.NEXUS).amount < 3 and self.can_afford(
                UnitTypeId.NEXUS):
            await self.expand_now()

    async def offensive_force_buildings(self):
        # print(self.iteration / self.ITERATIONS_PER_MINUTE)
        if self.units(UnitTypeId.PYLON).ready.exists:
            pylon = self.units(UnitTypeId.PYLON).ready.random

            if self.units(UnitTypeId.GATEWAY).ready.exists and not self.units(UnitTypeId.CYBERNETICSCORE):
                if self.can_afford(UnitTypeId.CYBERNETICSCORE) and not self.already_pending(UnitTypeId.CYBERNETICSCORE):
                    await self.build(UnitTypeId.CYBERNETICSCORE, near=pylon)

            elif len(self.units(UnitTypeId.GATEWAY)) < 1:
                if self.can_afford(UnitTypeId.GATEWAY) and not self.already_pending(UnitTypeId.GATEWAY):
                    await self.build(UnitTypeId.GATEWAY, near=pylon)
            if len(self.units(UnitTypeId.STARGATE)) < ((self.iteration / self.ITERATIONS_PER_MINUTE) / 2):
                if self.can_afford(UnitTypeId.STARGATE) and not self.already_pending(UnitTypeId.STARGATE):
                    await self.build(UnitTypeId.STARGATE, near=pylon)

            '''
            # 叮当
            if self.units(UnitTypeId.CYBERNETICSCORE).ready.exists:
                if len(self.units(UnitTypeId.ROBOTICSFACILITY)) < 1:
                    if self.can_afford(UnitTypeId.ROBOTICSFACILITY) and not self.already_pending(UnitTypeId.ROBOTICSFACILITY):
                        await self.build(UnitTypeId.ROBOTICSFACILITY, near=pylon)
            '''


    async def build_offensive_force(self):
        for sg in self.units(UnitTypeId.STARGATE).ready.noqueue:
            if self.can_afford(UnitTypeId.VOIDRAY) and self.supply_left > 0:
                await self.do(sg.train(UnitTypeId.VOIDRAY))

    def find_target(self, state):
        if len(self.known_enemy_units) > 0:
            return random.choice(self.known_enemy_units)
        elif len(self.known_enemy_structures) > 0:
            return random.choice(self.known_enemy_structures)
        else:
            return self.enemy_start_locations[0]

    async def attack(self):
        if len(self.units(UnitTypeId.VOIDRAY).idle) > 0:
            choice = random.randrange(0,4)
            target = False
            if self.iteration > self.do_something_after:
                if choice == 0:
                    wait = random.randrange(20,165)
                    self.do_something_after = self.iteration + wait
                elif choice == 1:
                    # 打基地
                    if len(self.known_enemy_units) > 0:
                        target = self.known_enemy_units.closest_to(random.choice(self.units(UnitTypeId.NEXUS)))
                elif choice == 2:
                    # 打建筑
                    if len(self.known_enemy_structures) > 0:
                        target = random.choice(self.known_enemy_structures)
                elif choice == 3:
                    # 打出生点
                    target = self.enemy_start_locations[0]
                if target:
                    for v in self.units(UnitTypeId.VOIDRAY).idle:
                        await self.do(v.attack(target))
                y = np.zeros(4)
                y[choice] = 1
                self.train_data.append([y,self.flipped])

        '''
        # {UNIT: [n to fight, n to defend]}
        aggressive_units = {UnitTypeId.VOIDRAY: [20, 3]}
        for UNIT in aggressive_units:
            for s in self.units(UNIT).idle:
                if self.units(UnitTypeId.VOIDRAY).amount > aggressive_units[UnitTypeId.VOIDRAY][0]:
                    await self.do(s.attack(self.find_target(self.state)))
        '''

    async def intel(self):
        print(self.game_info.map_size)
        game_data = np.zeros((self.game_info.map_size[1], self.game_info.map_size[0], 3), np.uint8)

        # draw unit map
        for unit_type in draw_dict:
            for unit in self.units(unit_type).ready:
                pos = unit.position
                cv2.circle(game_data,(int(pos[0]),int(pos[1])),draw_dict[unit_type][0],draw_dict[unit_type][1],-1)

        # draw enemy
        for enemy_building in self.known_enemy_structures:
            pos = enemy_building.position
            if enemy_building.name.lower() not in main_base_names:
                cv2.circle(game_data, (int(pos[0]), int(pos[1])), 5, (200, 50, 212), -1)
        for enemy_building in self.known_enemy_structures:
            pos = enemy_building.position
            if enemy_building.name.lower() in main_base_names:
                cv2.circle(game_data, (int(pos[0]), int(pos[1])), 15, (0, 0, 255), -1)

        for enemy_unit in self.known_enemy_units:
            if not enemy_unit.is_structure:
                worker_names = ["probe",
                                "scv",
                                "drone"]
                # if that unit is a PROBE, SCV, or DRONE... it's a worker
                pos = enemy_unit.position
                if enemy_unit.name.lower() in worker_names:
                    cv2.circle(game_data, (int(pos[0]), int(pos[1])), 1, (55, 0, 155), -1)
                else:
                    cv2.circle(game_data, (int(pos[0]), int(pos[1])), 3, (50, 0, 215), -1)

        for obs in self.units(UnitTypeId.OBSERVER).ready:
            pos = obs.position
            cv2.circle(game_data, (int(pos[0]), int(pos[1])), 1, (255, 255, 255), -1)

        # ratio test
        line_max = 50
        mineral_ratio = self.minerals / 1500
        if mineral_ratio > 1.0:
            mineral_ratio = 1.0

        vespene_ratio = self.vespene / 1500
        if vespene_ratio > 1.0:
            vaspene_ration = 1.0

        population_ratio = self.supply_left / self.supply_cap
        if population_ratio > 1.0:
            population_ratio = 1.0

        plausible_supply = self.supply_cap / 200.0
        military_weight = len(self.units(UnitTypeId.VOIDRAY)) / (self.supply_cap - self.supply_left)

        if military_weight > 1.0:
            military_weight = 1.0

        # worker / supply ratio
        cv2.line(game_data,(0,19),(int(line_max*military_weight),19),(250,250,200),3)
        # plausible supply (supply/200.0)
        cv2.line(game_data, (0, 15), (int(line_max*plausible_supply), 15), (220, 200, 200), 3)
        # population ratio (supply_left/supply)
        cv2.line(game_data, (0, 11), (int(line_max*population_ratio), 11), (150, 150, 150), 3)
        # gas / 1500
        cv2.line(game_data, (0, 7), (int(line_max*vespene_ratio), 7), (210, 200, 0), 3)
        # minerals minerals/1500
        cv2.line(game_data, (0, 3), (int(line_max*mineral_ratio), 3), (0, 255, 25), 3)

        # draw map bounder
        self.flipped = cv2.flip(game_data,0)
        if not HEADLESS:
            resized = cv2.resize(self.flipped, dsize=None, fx=2, fy=2)
            cv2.imshow('Intel',resized)
            cv2.waitKey(1)

        # show
        cv2.imshow('Intel', resized)
        cv2.waitKey(1)

    '''
    # 叮当
    async def scout(self):
        if len(self.units(UnitTypeId.OBSERVER)) > 0:
            scout = self.units(UnitTypeId.OBSERVER)[0]
            if scout.is_idle:
                enemy_location = self.enemy_start_locations[0]
                move_to = self.random_location_variance(enemy_location)
                print(move_to)
                await self.do(scout.move(move_to))

        else:
            for rf in self.units(UnitTypeId.ROBOTICSFACILITY).ready.noqueue:
                if self.can_afford(UnitTypeId.OBSERVER) and self.supply_left > 0:
                    await self.do(rf.train(UnitTypeId.OBSERVER))
    '''


    def on_end(self, game_result):
        print('--- on_end called ---')
        print(game_result)

        if game_result == Result.Victory:
            np.save("../train_data/{}.npy".format(str(int(time.time()))), np.array(self.train_data))


run_game(maps.get("AbyssalReefLE"), [
    Bot(Race.Protoss, SentdeBot()),
    Computer(Race.Zerg, Difficulty.VeryHard)
], realtime=False)
