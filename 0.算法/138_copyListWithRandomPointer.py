# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head:
            new_head = RandomListNode(head.label)
            new_head_repre = new_head
            head_repre = head
            node_list = [new_head]

            while head_repre.next:
                node = new_head_repre.next = RandomListNode(head_repre.next.label)
                new_head_repre = new_head_repre.next
                head_repre = head_repre.next
                node_list.append(node)
            head_repre2 = head
            memo = []
            idx = 0
            while head_repre2:
                memo.append(head_repre2.label)
                head_repre2.label = idx
                idx += 1
                head_repre2 = head_repre2.next
            new_head_repre2 = new_head
            head_repre3 = head
            while head_repre3:
                if head_repre3.random:
                    new_head_repre2.random = node_list[head_repre3.random.label]
                head_repre3 = head_repre3.next
                new_head_repre2 = new_head_repre2.next
            while head:
                head.label = memo.pop(0)
                head = head.next
            return new_head
        else:
            return

# with dic
'''
class Solution:
    def copyRandomList(self, head):
        dic = collections.defaultdict(lambda: RandomListNode(0))
        dic[None] = None
        n = head
        while n:
            dic[n].label = n.label
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next
        return dic[head]
'''


a = {79, 87, -300, -126, 470, 528, -343, 2, -256, -65, 82, 271, 13, 593, 65, -178, 204, 491, -8, 783, 219, -331, -296,
     -221, 196, 393, 359, 737, 306, 239, -259, -293, -130, 175, 391, 376, 501, 615, -375, 1, 754, 346, -4, -205, 333,
     242, 293, 253, 123, 428, -53, 597, -109, -335, -294, -289, -42, 5, 465, -37, -345, -217, 430, -352, -163, -20,
     -357, 85, 661, 182, 399, -206, 9, -224, 353, 434, 525, 591, 784, 267, 643, 726, 52, 34, 732, -129, 207, 259, -94,
     416, 311, 315, 680, 571, -303, -145, -133, -71, 205, 466, 247, 202, -180, 310, -382, -364, 452, -307, -338, -245,
     747, 562, 512, -66, -119, 463, -176, -134, -380, -189, -202, 51, -162, 596, 59, 343, -394, 408, -91, 422, 64, 229,
     -302, 524, 585, 610, -61, 536, -389, 208, 302, 487, -25, 347, 406, 78, 695, 62, -83, 166, -348, 538, -395, 132,
     -383, 702, 323, -99, -74, -223, -200, -156, 17, 560, -299, -125, -213, 37, -3, 4, 277, 513, 155, 700, 749, -273,
     70, -101, 105, -12, 236, 364, -143, 256, -97, 739, 197, -90, -211, 296, 617, 53, 109, 663, 460, 286, -257, 251,
     777, -19, 572, -1, 363, 23, -135, 785, 390, 101, 198, 383, 41, 405, 500, -229, 550, 515, 750, -263, -122, 283, 419,
     748, 652, -136, -351, -195, 425, 40, 246, 157, 210, 133, 139, 751, 342, 539, 565, 370, -334, 200, 488, -186, 636,
     131, 49, 701, 294, 580, 511, 679, -228, -393, 476, 462, -127, -172, 184, 563, 248, 775, 530, -276, 432, -70, 558,
     191, 187, -255, 455, 660, 305, 706, 612, 782, 631, 258, 233, 606, -381, -155, 228, -146, 703, -52, -76, 407, 261,
     411, 544, -165, -250, 224, 29, 352, 592, 384, 440, -181, -356, -6, 217, -111, 230, 154, 145, 555, 20, -271, -208,
     268, -233, 149, 746, -102, 141, 444, -118, 291, 392, -279, -151, 577, 535, 137, 728, -190, 468, 710, 322, -103,
     -374, 699, 287, 10, 415, -236, 708, 266, -120, -332, 647, -48, -315, 328, 222, -310, 683, -264, 273, -170, 417,
     -291, 534, -18, 389, 209, -212, 674, 245, -390, 658, 97, 745, 118, 704, 255, 651, -47, -31, 598, 640, 36, 478,
     -280, -355, 705, -188, 22, 74, 625, -388, 58, 576, 67, 281, 284, 609, 621, 340, 653, 72, 479, 533, 55, 379, -190,
     1, 87, 708, 739, -176, 705, 251, 580, 256, -74, -257, 29, 219, -211, -374, -178, 284, 72, 34, -332, 539, 703, -221,
     284, 236, -289, 680, 132, 101, 680, -25, 145, 534, 640, 228, -343, -119, -52, 4, 615, 625, 242, 560, 466, 737, 273,
     -102, -229, -357, 370, 29, -236, -233, 41, -118, -345, -125, 389, 534, 536, 737, 612, 562, -279, 598, 131, 609,
     539, -356, -381, 29, 182, 49, -6, 233, 501, 191, -307, -255, -289, 515, -393, 9, 283, 310, 281, 393, 323, -208,
     434, 9, 406, 528, -276, 703, 747, -145, 53, -129, 248, -90, 230, 284, -356, 455, 528, -18, 132, 422, -364, 87, 64,
     49, -119, 565, -364, 701, -389, 560, -393, -236, 376, 746, -83, 182, -151, 525, -345, 72, 10, -129, 528, 306, -181,
     22, -65, 58, 621, 23, 247, -343, 745, 79, 191, 775, -180, 2, -351, 525, 695, 17, -156, 706, 407, 754, 246, 463,
     293, 625, 750, 411, -352, -165, 563, 132, 463, -127, -20, 617, -6, 391, 51, 701, 391, 512, 236, 535, 452, 79, 311,
     -345 ,539,636,36,72,392,229,-122,-206,-374,563,488,306,425,184,430,530,2,-71,2,393,-165,205,315,248,-6,-279,550,411,-389,133,-212,703,97,631,562,550,428,137,609,434,-6,311,-256,536,-165,612,-181,615,572,705,72,389,706,-189,565,247,754,139,-111,-389,-355,271,62,643,-395,239,-307,572,-47,-120,105,683,-178,460,67,407,513,182,625,555,224,-229,478,782,-296,783,-176,34,-338,74,-233,363,-263,679,55,-19,501,679,-355,-188,-279,72,530,-291,-294,154,333,2,-289,333,533,-127,612,783,245,701,182,-170,137,370,101,352,571,535,536,-186,-134,750,-332,29,-118,-280,82,139,679,67,315,363,133,53,703,419,-357,408,-256,245,-101,-364,419,-364,118,511,271,-25,-53,-6,217,109,750,266,184,-129,465,87,-338,-1,-315,-395,-180,229,585,643,157,-190,708,-205,-176,683,428,-352,251,-130,-221,565,598,-257,-94,597,661,488,133,55,-348,596,-351,-122,463,640,-76,-294,-200,379,-245,-127,615,550,631,123,422,-224,-303,229}
