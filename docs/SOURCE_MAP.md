# 当前源码地图

这些是当前仓库实际存在的入口，名称描述仅用于导航；修改前继续核对函数消费者和实际作用域。

|关注点|入口|
|---|---|
|宫帐政体定义|[zz_nhe19_steppe.txt](../pgh_accounts/common/governments/zz_nhe19_steppe.txt)|
|宫帐独立庄园|[zz_nhe72_palace_estate.txt](../pgh_accounts/common/domiciles/types/zz_nhe72_palace_estate.txt)|
|普通庄园定义|[zz_nhe19_estate.txt](../pgh_accounts/common/domiciles/types/zz_nhe19_estate.txt)|
|回调入口|[nhe19_on_actions.txt](../pgh_accounts/common/on_action/nhe19_on_actions.txt)|
|账户/载体生命周期|[nhe19_lifecycle.txt](../pgh_accounts/common/scripted_effects/nhe19_lifecycle.txt)|
|自动维护|[nhe45_automatic.txt](../pgh_accounts/common/scripted_effects/nhe45_automatic.txt)|
|住所类型识别|[zz_nhe72_estate_types.txt](../pgh_accounts/common/scripted_triggers/zz_nhe72_estate_types.txt)|
|庄园初始化扩展|[zz_nhe72_estate_setup.txt](../pgh_accounts/common/scripted_effects/zz_nhe72_estate_setup.txt)|
|军事页|[window_military.gui](../pgh_accounts/gui/window_military.gui)|
|募兵页|[window_menatarms_type_view.gui](../pgh_accounts/gui/window_menatarms_type_view.gui)|
|住所管理器|[nhe47_md_manager.gui](../pgh_accounts/gui/nhe47_md_manager.gui)|
|建筑/交换入口|[nhe47_md_core_effects.txt](../pgh_accounts/common/scripted_effects/nhe47_md_core_effects.txt)|
|界面条件宏|[mpo_macros.txt](../pgh_accounts/data_binding/mpo_macros.txt)|
|本地化补漏|[简体中文](../pgh_accounts/localization/simp_chinese/nhe72_palace_estate_l_simp_chinese.yml)、[英文](../pgh_accounts/localization/english/nhe72_palace_estate_l_english.yml)|

`docs/architecture/`中的旧PGH `pgh_*` 调用链分析包含未打包的旧源码引用。它解释历史研究，不是当前 `nhe*` 文件的完整调用图；不要按旧行号修改当前代码。
