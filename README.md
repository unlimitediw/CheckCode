# 项目及部分日常代码
> @unlimitediw 李文韬
* P.s 经过早上和hr的沟通，发现确实存在压缩包中数据，包繁杂，可读性低的问题。作为改进，新包将只存在txt(README)，md(云计算项目)，pdf(报告)和代码文件，均为自己完成，合作完成项目会特别注明。——2019-01-22 GMT8

* 0-8主要针对简历上的项目以及个人经历一一简要介绍
* 9为部分日常代码以及诸如c,js,css,ruby与pl等语言的练习。


### 0. [算法](https://github.com/unlimitediw/CheckCode/tree/master/0.%E7%AE%97%E6%B3%95)
* 简介：包含如backtracking，动态规划，树结构等各类算法。此文档所存是2018年7-10月使用python实现的算法，而在2018年1-2月的算法均使用c++实现，近期主要使用java完成算法工作。leetcode目前完成476题（unlimitediw)，其中medium&hard占比65%。每周leetcode contest前三道（一般为双medium，hard）均可在一个小时内完成，第四道hard看运气。

### 1. [城市数据预测](https://github.com/unlimitediw/CheckCode/tree/master/1.%E5%9F%8E%E5%B8%82%E6%95%B0%E6%8D%AE%E9%A2%84%E6%B5%8B)
* 简介：主要分为 - 1.基于SVR与MLP的数值预测部分; 2.基于CNN的特征验证部分。
* 内容：项目报告(pdf)，测试代码(Predictor.py)，smo调参算法代码(MySMO.py)，mlp调参算法代码（MLPGenerator.py)，基于CNN的特征评估(mapToPopulation.py)，部分数据抓取(Search.py)，数据预处理(DataPreprocessing.py)，信息熵计算器(EntropyGainGenerator.py)，kfold(KfoldValidation.py)测试代码，以及现写的数据可视化(Visualization.py)等代码。

### 2. [AWS项目开发](https://github.com/unlimitediw/CheckCode/tree/master/2.AWS%E9%A1%B9%E7%9B%AE%E5%BC%80%E5%8F%91)
* 简介：
	* AWS亚马逊网络服务平台是美国目前最大的云计算服务平台，本项目组主要集中于 i. 基于AWS redshift, hadoop及Lambda等工具的实时数据流分析处理，以及机器学习训练代码部署与分析;(BigDataMachineLearning.md, SageMakerTechReport.md) ii. Container的部署与管理，结合网页开发的应用项目，使用了swarm，Kubernetes等工具。(DockerContainer.md)。
	* 项目主要目的是掌握aws中的各类api使用及原理。结合使用linux系统操作各类工具系统达成数据流处理，机器学习，服务器搭建等各类项目任务。

### 3. [各类机器学习项目](https://github.com/unlimitediw/CheckCode/tree/master/3.%E5%90%84%E7%B1%BB%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E4%BB%A3%E7%A0%81)
* 简介：各类机器学习小项目。
* 内容：PIMA疾病预测(PimaKmeans.py, PimaKNN.py),MNIST-PCA数字预测(MNISTMLP.py,MNISTKNN.py,MNISTKmeans.py), 肝病预测(LiverMLP.py),工资预测(SalarySVM.py,SalaryMLP.py), 猫狗分类(CatDogCNN.py),目标检测-基于api(RecognitionRCNN.py),车辆识别-预处理阶段(CarImgPreProcess.py,CarImageBuild.py),行走学习(QLearningBasic.java)等。

### 4. [游戏AI平台](https://github.com/unlimitediw/CheckCode/tree/master/4.%E6%B8%B8%E6%88%8FAI%E5%B9%B3%E5%8F%B0)
* 简介：设计了一系列棋类游戏AI和部分玩家对战接口，负责所有算法和sql部分，服务器客户端和notexponential部分是和同伴共同完成。
* 内容：三个AI - a.NPuzzle(NPuzzleAI.py), b.NTicTacToe(NTicaTacToeAI/AI.java,OptimalList.java等), c.NQueen,一个交流服务器客户端(KVStorer/),一个sql小论坛(SuggestionBoxSQL.java),一个notexponetial接口(not exponential.java)。

### 5. [SC2AI](https://github.com/unlimitediw/CheckCode/tree/master/5.SC2AI)
* 简介：请预装星际争霸2并设置好系统路径,预装sc2Start中调用的包。
* 内容：运行sc2Start会自动生成游戏进行选择难度进行对战(sc2Start.py)，sc获胜思路是，设计运营公式，使用空中单位(规避地形问题)。

### 6. [基于机器学习的CPU分支预测](https://github.com/unlimitediw/CheckCode/tree/master/6.%E5%9F%BA%E4%BA%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E7%9A%84CPU%E5%88%86%E6%94%AF%E9%A2%84%E6%B5%8B)
* 简介：使用程序运行中的trace地址记录文件，预测下次分支走向。
* 内容：trace文件转换(Trace_Initializer.py)，地址记录器(Register.py),权重生成。（Perceptron_Table.py),感知机方法（Perceptron.py),LVQ方法(LVQ.py)。cadence优化方面如有需要我可以去实验室拿我做的模型。

### 7. [基因预测](https://github.com/unlimitediw/CheckCode/tree/master/7.%E5%9F%BA%E4%BA%8EHMM%E7%9A%84%E5%9F%BA%E5%9B%A0%E9%A2%84%E6%B5%8B)
* 简介：基因分coding和non-coding，本项目旨在使用上一次基因片段顺序，关联概率预测下一次片段是coding还是noncoding。
* 内容：HMM.py中包含解释

### 8. [游戏设计](https://github.com/unlimitediw/CheckCode/tree/master/8.cs%E6%B8%B8%E6%88%8F%E8%84%9A%E6%9C%AC)
* 简介：2016年至2018年之间，运用C#设计了rpg游戏，rts手游及各类小游戏，部分脚本存在这个文件夹中。
* 内容：各类脚本（文件夹内大概为总量的15%)

### 9. [Other](https://github.com/unlimitediw/CheckCode/tree/master/9.Other)
* 简介：部分日常代码。
























