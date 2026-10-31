> 归档提示：本文的“当前”、执行顺序、旧run路径和未实现状态均属于当时记录。未打包的旧路径不可在本仓库执行；不要恢复已取消计划。现行任务以 [当前交接](../HANDOFF.md) 和 [下一步](../NEXT_STEPS.md) 为准。

> 历史设计资料；机器路径已移除。当前验收以 docs/VALIDATION.md 为准。

# 当前验收口径补充（ACCEPTANCE-002）

原始PGH代码语义调查保留如下。执行顺序以 runs/ACCEPTANCE002/剩余计划与最小场景.md 为准：不再先做GUI精度或原生自然收入公式测试。资产保护、容量拒绝、有限维护、防重复和失败恢复语义仍保留；本文历史“精确差额”描述是源码事实，不构成新增引擎数字回归要求。本轮只改文档，不改源码。

# PGH真实调用链与本项目边界

来源为runs/R05已冻结的PGH_SOURCE，本轮复制到baseline/PGH_SOURCE并逐文件保存指纹。这是当前项目已批准研究的具体快照；没有声称远端Workshop版本一致，也没有改正式PGH。判断以实际分支语句为准，不能只读注释。

## 默认死亡路径

on_actions文件:16把on_death追加到pgh_before_death；:277–319定义实际分支。独立角色调用R29H；非独立且is_governor=yes、steppe_admin_government的角色默认B2释放。如果角色pgh_b2_global_off存在，才走S9余额托管。附近STEP9旧注释仍写value-only，但默认执行语句已经是B2，不能按注释推翻执行分支。

B2 release/regrant effects:30起保存临终角色、top_liege、ordinary primary office、实际受保护AUX；:89附近以stepped_down构建并resolve头衔事务；核验上级真持有后才写office→pending_aux、aux→pending_office追踪。on_title_gain注册的pgh_b2_regrant_aux_gain在on_actions:360–368检测**实际刚获得office的角色**，再用granted授予同一AUX；完成后更新绑定、清pending、标pool_consumed。任命对象不是死前预测current_heir，不应改用“最有威望/牧群最多者”。

原B2保存主职衔、角色与辅助头衔的精确引用值得复用；本项目新的非世族county载体不等于is_nomad_title，不得照搬游牧筛选。须按唯一受管理标记+精确双向绑定定位，先证明是真实非独立总督和实际普通职衔。R05 67619仅持县不构成此证据，不能当成实际宫帐任命样本。

原B2迟延5天清理事件仍会被调度，但pgh_b2_cleanup_pool_now_effect:895附近已是安全延后/非破坏体；一人一账户consolidate:1048也是always=no，on_actions季度调用被注释。不能因注释写“并入+销毁”就把现行清理说成自动安全合并。30天列表和400天追踪属于旧实现，不直接搬为新系统轮询/保活成本。

## 独立统治者

R29H before_death:6–75要求独立宫帐角色、王国及以上ordinary primary且current_heir存在；读取真实原生住所余额，先stage再实际扣至0，确认后ordinary primary上标ready。current_heir这里只是前置存在检查，不是指定最终收款对象。

on_title_gain与on_title_gain_inheritance都注册R29H claim，按实际得到带ready普通头衔的人排队，2天后settle；锁避免双调。settle要求当前实际持有该普通主头衔的适格角色，验证接收账户、容量余量、到账精确差额才消费托管。每天有限重试最多7次，失败保留托管并转人工复核。它只承诺余额，不重建住所ID、建筑、文化信仰或头衔兵；这些资产不能冒充已转交。

该路线若迁移到本项目，只改精确对象解析与新政体资格，不改变“真实主职衔决定实际继承人、确认扣款才可付、实际到账才消费”的语义。新项目主要宫帐总督分支不应擅自改为R29H；独立路线另建样本、另验收。

## 合并安全

B2 regrant:220–246附近在新持有人已有账户时，直接给其住所change_herd并destroy incoming title，缺少容量、源余额归零和头衔兵门槛；不能直接迁移。它是真实源代码存在的危险分支，不等于本项目已批准忽略资源安全。

PGH effects R27:637起旧独立handoff不是当前默认on_death，但其中:708–766提供可复用的安全事务原则：目标room=max_herd-herd且非负；source<=room；source无任何title-MAA；保存两端前值；先目标加、源减；确认目标精确增加且源0之后才销毁；失败尝试恢复两端并保留源。保留第二账户属于资产保护例外，不能为了“一人一账户”删真实兵或建筑。

本项目合并目标必须来自已批准的精确绑定，不照搬旧R27按herd排序挑目标。NF是独立家族资产，不能选作合并源/目的，也不能销毁；动态载体与NF共存不构成重复待清理对象。非默认/新增建筑、地点或其他资产有差异时先拒绝余额式销毁，原PGH R27并未提供完整建筑合并规则。

实现顺序：先只读取证/自然收入归属；再为真实任命/死亡事件挂精确有限维护；最后安全合并。没有world every_living轮询、季度牧群结算、骑手手工扩缩或隐藏补差。当前只准备场景与断言，生命周期迁移代码没有落入候选，仍NOT IMPLEMENTED/NOT RUN。
