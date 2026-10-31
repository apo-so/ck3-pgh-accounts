# 开发说明

唯一接手入口为 [接手入口](../接手入口.md)，具体当前步骤见 [NEXT_STEPS](NEXT_STEPS.md)。

## 本次上传的源码基线

本仓库为当前工程的完整源码快照，不是只有两文件的补丁。R72完整候选叠加R76两文件覆盖层；原文件字节、BOM与换行保持。`source-manifest.json` 记录发布源码哈希，执行 `python tools/verify_manifest.py` 可核验。

## 源码入口

- `common/domiciles/types/`、`common/domiciles/buildings/`：住所类型及建筑。
- `common/on_action/`：入口回调；`common/scripted_effects/`、`common/scripted_triggers/`：生命周期与作用域逻辑。
- `common/scripted_guis/`、`gui/`：脚本界面及窗口。按实际文件追溯作用域与消费者。
- `localization/`：简体中文和英文。R76新增 nhe72_palace_estate_domicile_type 键。

## 修改与验证原则

先复用现有完整功能路径。默认不增加玩法门槛；引擎硬限制、明确需求或实际问题才引入必要条件。原生住所头衔保护保留。
分别报告源码完成、静态检查、部署读回、实际加载、场景行为与界面验收。不得把哈希核验当作运行验证。
先核对当前Mod与游戏版本，再将反馈日志关联到实际源码。旧R2/R3日志不是当前快照的测试结果。

## 文档关系

`architecture/`为原工程机制与设计文档的脱敏快照，部分形成于更早阶段，仅用于理解设计与历史理由。它们不是新的验收结论；当前源码与 VALIDATION.md 为本次上传范围依据。

## 未上传的本机工程材料

存档、完整大日志、机器路径、凭据、部署回滚备份及重复候选留在本机工程。此仓库提供继续开发所需源码与说明，不包含完整本机操作历史或原生测试证据全集。
