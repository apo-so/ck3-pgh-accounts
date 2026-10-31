# 安装

1. 备份现有同名 Mod，避免与创意工坊同一 Mod 重复启用。
2. 将仓库 `pgh_accounts` 文件夹复制到 CK3 用户目录的 `mod` 文件夹。
3. 在同一 `mod` 文件夹放入仓库根部的 `pgh_accounts.mod`。其相对路径为 `mod/pgh_accounts`，不含作者机器绝对路径。
4. 在 Launcher 中启用本地 Mod 后启动游戏。检查实际载入版本，保留问题复现日志。

描述符标记支持1.20.*，历史验证范围见 VALIDATION.md；旧存档迁移及第三方Mod兼容性没有全覆盖保证。

## 当前自动新建账户链的适用条件

当前 [nhe19_new_office_trigger](../pgh_accounts/common/scripted_triggers/nhe19_triggers.txt) 要求 `has_tgp_dlc_trigger = yes` 和 `has_mpo_dlc_trigger = yes`。准备测试自动新建职衔账户时，应先核对这两项DLC状态；仓库没有全DLC组合的运行验证。

同文件的 `nhe46_steppe_realm_trigger` 要求角色存活、未进入临终标记、为 `steppe_admin_government`（宫帐政体）、有地，且领地内至少一县属于 `the_great_steppe` 情势。不要求首府在大草原；独立统治者也在此路径设计范围。职衔还需满足 `nhe19_ordinary_office_trigger`，具体以源码为准。

这些是当前源码中“自动新建账户”这一条路径的既有条件，不是所有界面功能的全局条件。本轮只补说明。排错时先区分不满足现有触发条件、函数未进入、进入后失败和纯日志预警。
