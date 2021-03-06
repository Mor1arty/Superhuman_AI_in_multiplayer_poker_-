'''多人扑克领域的超强AI

近年来有很大的进步在人工智能方面，游戏经常被作为进步的挑战性的问题、基准、里程碑。扑克作为一个有挑战性的问题已经几十年了。过去被作为成功的基准，包括扑克，一直被限制在两个玩家的游戏中。然而在 传统游戏中，扑克一般都是多于两人的多人游戏。多人游戏提出了更多基础性的额外的问题远远超出了二人对弈游戏，多玩家扑克被认为是AI的一个里程碑。这篇论文我们展示了Pluribus，一个可以在六人无限制德州扑克（一种在北美非常受欢迎的扑克玩法）中战胜人类顶尖专家的人工智能。

扑克提供了一个挑战性的问题在人工智能领域和游戏领域已经数十年了。事实上，在游戏理论的基础论文里面就用扑克说明他们的概念。选择扑克的原因是简单的，没有其他的流行的娱乐性游戏具有这么多挑战在隐藏信息方面，如此有效，如此优雅就像扑克一样。尽管扑克曾见作为新AI和游戏理论技术方面的基准，隐藏信息的策略设置方面挑战在 不仅仅局限于娱乐性的游戏。平衡的概念被冯诺依曼和纳什应用到了很多真实世界的挑战中，例如拍卖，网络安全，和定价。
过去的二十年我们见证了在AI系统玩不断增加的复杂形式的扑克的快速进步。然而，所有的先前的突破都是被限制在仅有两个玩家上。发展一个超级人工智能在多人扑克领域被广泛的认为是主要的剩余的里程碑。在这篇论文里面，我们描述了Pluribus，一个在六人无限制德州扑克中有能力击败人类专家的AI。



在多人游戏中的理论和实践上的挑战。

AI系统在很多游戏中达到了超人的表现，例如checkers，棋类，两人限制扑克，GO，和两人无限制扑克。所有的这些游戏都是两人游戏，并且是零和游戏（即一方赢，另一方就要输的游戏）。每一个这些超强的AI系统都是通过尝试找到一个近似的纳什均衡来实现，而不是通过其他一些策略，例如尝试发现和探索对手的弱点。纳什均衡是一系列的策略，一个为所有玩家制定的策略，没有任何玩家可以通过改变纳什均衡而到一个不同的策略而获得提升。纳什均衡已经被证明存在于所有的“有限”游戏中，和许多“无限”游戏中，尽管发现一个均衡有时可能是困难的。

两人零和游戏是游戏中的一个特殊的类别，在两人零和游戏中，纳什均衡有一个非常有趣且有用的特点，即不管对手怎么做，使用纳什均衡策略的玩家必然不会输（只要不存在一方在游戏规则之下有固有的优势，或者玩家交换方向）。换句话说，只要满足标准，纳什均衡策略在两人零和游戏中是无敌的。因此，解决一个两人零和游戏就意味着找到构造一个准确的纳什均衡的方法。例如，把纳什均衡用在剪刀石头布上，即以等概率随机的选取剪刀，石头，布。为了对抗这种策略，他的对手最好的期望就是平局。在这个案例中，选用纳什均衡同样也保证了玩家在期望上不会赢。然而在更复杂的游戏中决定怎样平局对抗纳什均衡甚至也是很困难的。如果你的对手选取了次优的策略，选取纳什均衡的人在期望上确实会赢。

原则上，使用纳什均衡可以结合对手探索，通过最初的纳什均衡策略并且在接下来的时间里转换策略针对已经观察到的对手的弱点（例如，通过转换到大概率出布的策略来克制对手的大概率出石头的策略）。然而，除非在确定的被限制的方向，转换到一个剥削性的非纳什均衡的策略同时会使自身陷入可被剥削的境地，因为对手也可以随时转换策略。另外，AI使用对手剥削的技术需要太多的案例，才能与外部的人类专家竞争。Pluribus使用了一种修正的策略，这种策略不采用观察对手倾向的方式。

尽管纳什均衡策略被确证存在于任何有限游戏中，高效地寻找那时候均衡的算法目前只存在于某些特殊的游戏类别里面，其中，二人零和游戏是最突出的。在二人零和游戏中至今没有一种多项式时间复杂度的寻找纳什均衡的算法是被公认的。如果你发现其中的一种，那你将会横扫计算复杂度理论。发现一个纳什均衡在三人甚至多人零和博弈中至少是困难的（因为一个模拟的玩家将会被加入游戏，使游戏变为三人零和博弈），甚至近似一个纳什均衡都是困难的（除了一些特殊的例子）在理论上和在超过两个玩家的游戏中。甚至最完整的算法也只能很少的可能的策略来处理游戏。此外，甚至如果一个纳什均衡可以在不超过两个玩家的情况下被高效的计算出来，那也不清楚执行这样一个计算出来的策略是不是明智的。如果每一个玩家独立玩游戏，各算各的，他们每个人都独立算纳什均衡，他们策略的步骤在全局上来看可能都不是一个纳什均衡，每位玩家可能有一个激励使他们偏离至不同的策略。其中的一个例子就是柠檬水摊游戏，说明在图一。这个游戏中，每位玩家同时在圆环上面选取一个点，使得他的点尽可能离别人的点更远。对所有玩家的纳什均衡是放置点均匀地于圆环之上，但这有无限种可能性，有无限种拜访方法。如果每个玩家独立地计算各自的纳什均衡，联合的策略就不再是对所有玩家的纳什均衡那样均匀地分布在圆环上了。两玩家零和博弈是一个玩家独立计算和选择纳什均衡，策略的全局依旧是一个纳什均衡的特例。

纳什均衡有解决两玩家零和博弈游戏之外的短板，其他游戏理论也未能令人信服地克服了它们，什么是游戏种正确的目标被提到了问题的表面。在六人扑克的案例中，我们采取的观点是不应该采取一个特殊的游戏理论解决概念，更确切地说是创造一个AI经验性地一贯地击败人类对手，包括精英人类专家。

我们构造Pluribus的算法将在下俩节讨论，不保证将会汇聚于两玩家零和博弈之外的纳什均衡。尽管如此，我们观察到Pluribus扮演了一个重要的策略在多人扑克上，它有能力持续地击败人类的专家级选手。它说明了即使在两玩家零和博弈领域之外没有强有力的理论保证，我们仍有可能在更宽广的策略设置领域制造出超强的AI。


Pluribus的描述

Pluribus的核心是通过自我博弈来计算的，即AI对抗他们的复制体，不输入任何人类或者先前的AI的博弈数据。AI通过随机下棋开始，逐渐提升以决定他们之后的动作，和那些可能的分布在这些动作之后，通向比它们曾经的版本更好的策略。自我博弈的形式很早以前就被用在制造两人零和博弈中的超强AI，例如backgammon,Go ,刀塔2，星际争霸2，和两人扑克，虽然这个精确的算法被用在很宽广的范围。尽管在二人博弈中用自我对弈构造一个简单的工具是容易的，但这并不能得出一个有意义的结论。尽管自我博弈已经在二人对弈中展现了一个足够好的结果。

Pluribus的自我博弈离线地为整个游戏产出了一个策略，我们把它叫做蓝图策略。当真实的游戏开始后，Pluribus在蓝图的基础上根据自身所处的情形实时搜索更好的策略。下面的小节我们将在细节上讨论所有的阶段，最开始我们讨论抽象，一种我们用来使每个阶段可扩展的方法。


大规模不完整信息游戏中的抽象

因为不独立的原因无限制德州扑克中有太多的决定点了，为了降低游戏的复杂性，我们消除了一些动作并且把相似的动作归类，这一过程称为抽象。抽象之后，那些归为一类的决策点被认为是相同的。在Pluribus中我们使用了两种抽象，动作抽象和信息抽象。

动作抽象降低了AI需要考虑的动作的数量。无限制德州扑克通常允许在100美元到10000美元之间的任意金额的下注。然而，在实际中下注200美元和下注201美元没有很大的差异。为了减少形成一个策略的复杂性，Pluribus通常只会设定很少的几种下注的金额大小。准确的下注的数量在一到十四之间根据实际状况而定。尽管Pluribus可以限制自身在100美元到10000美元之间以少数几种固定的金额来下注，但当真正玩无限制德州扑克时，它的对手不会被限制在这几种金额上。当Pluribus只能押100美元和200美元是，它的对手押150美元时会怎么样？通常说，Pluribus会依赖它的搜索算法，这个算法在后面的小节会讲到，为“树外操作”（off-tree action)实时算出一个回应。

另一种我们使用在Pluribus中的抽象是信息抽象。在扑克中那些可以被归为一类的牌将被同等对待。例如一个十高桥和一个九高桥牌面上是不同的，但是战略意义上是相似的。Pluribus尽可能把这些牌捆绑在一起，并以同样的方式对待它们。因此在决策时可以减少不同状态的数量。信息抽象大量地减少了游戏的复杂性，但是可能清洗掉了牌中的一些微妙的不同，对于超人表现，这很可能是重要的。因此在实际的对抗人类的过程中，Pluribus仅仅在推理未来的下注轮时被使用到，在实际本轮次中一点也不使用信息抽象。信息抽象也被用在树外自玩之中。


通过蒙特卡罗反事实缺憾最小化方法的自学习

Pluribus中的蓝图策略是通过蒙特卡罗反事实缺憾最小化方法计算的。CFR是一种迭代的自玩算法，AI以完全地随机开始，通过学习来打败自己更早的版本以获得提高。过去六年里每一个竞争性的德州扑克AI都是通过CFR算法的变种来计算自己的策略。我们使用一种MCCFR的变种，它简化游戏树里面的动作，而不是遍历全部的在每个迭代里的游戏树。

在算法的每一个迭代里面，MCCFR指定一个玩家作为转盘，它的现在执行的策略在迭代时将被更新。在一个迭代的开始，MCCFR基于现在的策略给所有的玩家模拟一手牌（在开始时这是完全随机的）。一旦手牌模拟完成，AI就开始回顾转盘所作的每一个决定，并且通过选择其他可能的动作代替已经做过的动作，来调查已经做的动作有多好或者多坏。接下来，AI回顾每一个在可获得的动作之后假定的决定，并且评价它有多好或者多坏通过选择其他可获得的动作，反复如此。遍历的游戏树的说明在图二中。探索其他假定的结果也是可能的，因为AI知道每一个玩家在迭代中的策略，因此可以估计用其他动作代替这个动作将会发生什么。这种反事实的推理是CRF和其他用在GO，Dota2, StarCraft2中的自玩算法的区别所在。

轮盘获得的可能的动作和轮盘在迭代时实际上获得的动作的不同在于，是否在动作中计入了反事实缺憾。反事实缺憾代表着轮盘对在前面的迭代中没有选区的动作的遗憾多少。当迭代结束时，轮盘的策略被更新，那些具有更高的反事实缺憾的动作有更高的可能性被选取。

对于二人零和游戏，CFR确保平均的策略将所有的迭代重演，并将其汇聚到一个纳什均衡上面。但是在两人零和游戏之外不能确保这种汇聚。尽管如此，CFR保证了在有限游戏种，随着迭代次数的增多，反事实缺憾次线性的生长。这在一定程度上保证了每一次迭代的平均性能都是事后最佳单修正策略的平均性能。CFR也被证明用在有限游戏种以消除迭代性的严格的控制动作。

因为，反事实值和期望值的不同在于，反事实值是对反事实缺憾的补存，而不是代替它。在第一次迭代的时候，代理人都是完全随机地玩牌（往往它会打的一手烂牌），但这仍然影响着反事实缺憾。因此，刚第一次迭代运行的策略和未来的迭代种的策略往往相去甚远。在CFR的一般形式中，第一次迭代的影响会衰减到原来的１／Ｔ，T是迭代的数目。为了尽快把最初坏迭代的的影响消除，Pluribus使用了一种近来的CFR的形式，线性CFR，在早期的迭代中，（在此之后，我们停止贴现，因为用贴现系数做乘数的时间成本不值得以后的收益）。线性CFR将权重T分配给每一代的缺憾贡献。因此第一代的衰减率就降为了１／add(t)==2/T(T+1)。这使得策略明显更快速地提高，同时维持几乎完全相同的最坏边界在整个缺憾上。为了更进一步提升蓝图策略计算的速度，那些非常消极的遗憾在百分之九十五的迭代里将不会被探索。

Pluribus的蓝图在一个64核的服务器上总共计算了八天，共计12400个CPU核心小时。需要不小于512G的存储空间。用现在用计算流行的实体速率来计算，只要144美元就可以计算出来。这与现在流行的其他使用了大量算力的超强AI里程碑游戏相比较而言是非常鲜明的。更多的内存和算力可以产生更细粒度的蓝图，但这同样造成Pluribus使用更多的内存或者在实时搜索时速度会降低。我们将蓝图策略抽象的大小设置到允许Pluribus在实时游戏中运行，运行的机器需要不超过128G的内存用来存储压缩后的蓝图策略。


深度受限搜索在不完全信息游戏中的运用

受限于无限制德州扑克的大小和复杂度，蓝图对于整个游戏来说是粗粒度的。Pluribus仅仅在第一轮里面根据蓝图策略出牌，这时决策点的数目很小以至于可以直接使用蓝图策略，不必使用信息抽象和行为抽象。在第一轮之后（甚至是第一轮如果你的对手选取和蓝图里面动作抽象完全不同的赌注大小）Pluribus将实施实时搜索来为当前所处的环境选取一个更好的更细粒度的策略。对于第一轮中对手赌注数量明显在树外的情况，Pluribus将押注在其接近树的大小上，并继续玩当它的对手使用了之后的赌注大小。

实时搜索对于AI在不完全信息游戏中的超人表现是非常重要的，这些游戏有backgammon ,chess,和Go。例如，棋类AI在决定下一步的走法时，通常会向前看几步直到算法的深度限制的叶子结点。然后，如果两个玩家都要从这一点向前玩纳什均衡，会具有评估功能，并会估计叶子节点处的板配置值。 原则上，如果AI可以精确地计算出每个叶子结点的值，算法就可以选取最优的下一步。

然而，将完美信息游戏中的搜索策略用在不完美游戏中基本上是失效的。例如，考虑一种相继形式的石头剪刀布，说明在图三中，玩家一先选取动作，但是不透露他的动作给玩家二，接下来玩家二选取动作。如果玩家一预测一步，那么它每一个叶子结点的值的和都是零，毕竟，如果玩家二如果选取纳什均衡的策略的话，选取每个动作的可能性都是三分之一。所以玩家一的策略可以选择总是出石头，因为它的表现和其他的策略是相同的。

的确，如果玩家二永远使用纳什均衡，那么只出石头对于玩家一来说是最好的策略之一。然而，实际中，玩家二可以调整他的策略 为只出布。在这种情况下玩家一的值就变为了-1。

这个例子说明，在不完美信息子游戏中（即进行搜索的游戏的部分），叶子结点没有修正值。相反地，这个值取决于搜索者在搜索中采用的策略。在原则上，这可以通过根据搜索者在游戏中的策略构造一个部分游戏结点的函数来确定。但是这在大型游戏中是不可行的。另一种选择是使叶节点的值仅以两个玩家在游戏中那一点的信念分布为条件。这是用来生成两个玩家扑克的人工智能Deepstack。然而，这种选择是极端昂贵的，因为这需要在信念的条件下解决数量巨大的子游戏。在隐藏信息和玩家的数量增长时这种方法付出的代价甚至会更加地昂贵。两人扑克AI天秤座回避了这个问题，只在剩下的游戏足够短，深度限制将延长到游戏结束时进行实时搜索。然而，随着玩家数量的增加，一直到游戏结束的解决方案也变得难以计算。



'''
