> 历史初审：以下结论针对提交 `2adc0857ea961c89f091a95f996a57ed2b74c3ae`。修复与复核状态见 [审查闭环](README.md)。独立审查者临时目录已脱敏。

# GitHub-only 独立接手审查报告

审查对象：https://github.com/apo-so/ck3-pgh-accounts

固定提交：`2adc0857ea961c89f091a95f996a57ed2b74c3ae`，提交标题 `Add standalone project handoff, source map and historical evidence`，提交时间 2026-10-31 18:40:45 +08:00。

审查目录：`[INDEPENDENT_REVIEW_DIRECTORY]`。

## 结论

|层次|结论|含义|
|---|---|---|
|仅凭仓库开始源码接手|PASS|可定位当前源码、现行状态、正确下一步和需保留的历史边界；无需原作者本机项目、技能、安装目录或旧聊天。|
|当前原始快照字节完整性|PASS|69个Mod文件和外置描述符均实际存在，与70项清单相符。两份原仓库工具均退出0。|
|现有自动核验闸门的抗遗漏能力|PARTIAL|清单缺项与空历史证据清单可逃过检查，见F1、F2；当前固定快照未出现这两种缺陷。|
|源码结构补充检查|PASS_LIMITED|全部Mod文本做词法结构扫描；GUI自定义脚本引用、本地化BOM/头与R76当前字节对应已交叉检查。不是CK3编译或作用域语义证明。|
|历史结果可读性|PASS|R59、R72、R74、R76各自观察范围与未覆盖范围可辨认。|
|历史运行结果绑定当前全部源码|PARTIAL|R76可绑定两文件实际字节；R59/R74摘录不能单独建立全部被测源码与加载集合的链，见F4。|
|新机器安装/部署/实际加载|NOT_RUN|本审查未写安装目录，也未运行游戏。|
|游戏场景、渲染、用户验收|NOT_RUN|没有把哈希、源码链或历史JSON当作本次运行通过。|
|复现反馈的当前报错|NOT_RUN|仓库缺少当前反馈错误原文和实际环境身份；NEXT_STEPS明确让接手者先归因，不能凭旧日志修当前源码。|

没有发现足以阻止首次源码接手的P0/P1项。以下P2项可在仓库内修复；不需要为了修文档或核验工具启动游戏。

## 获取方式与隔离边界

先通过 `git ls-remote https://github.com/apo-so/ck3-pgh-accounts.git HEAD` 得到以上SHA。随后在全新Temp目录内 `git init`，添加公开HTTPS remote，按完整SHA浅取，再detached checkout。没有使用或读取任何现有本地clone、主代理工程、记忆、原作者安装目录、原生存档或旧聊天。GitHub网页也通过只读HTTPS打开，用于确认公开仓库身份。

审查保留的原始检出为 `repository/`。审查脚本和结果均在它的父目录。异常输入试验仅在 `fixtures/` 下新复制的私有测试副本进行。原始检出最终 `git status --porcelain=v1` 为空。未修改远端、未部署、未启动或控制游戏。

## 实际执行与结果

环境：PowerShell，Python 3.13.3。仓库两个工具只依赖标准库，本次未安装Python依赖。

下载命令（按顺序，工作目录为新建的 `repository/`）：

```powershell
git init
git remote add origin https://github.com/apo-so/ck3-pgh-accounts.git
git fetch --depth 1 origin 2adc0857ea961c89f091a95f996a57ed2b74c3ae
git checkout --detach FETCH_HEAD
git rev-parse HEAD
git status --porcelain=v1
```

均成功，HEAD精确匹配，初始工作树干净。下载原始输出见 `logs/OP01-download.txt`。

|实际命令|退出码/结果|证据|
|---|---|---|
|`python --version`|0，3.13.3|logs/OP02-baseline.txt|
|`python tools/verify_handoff.py`|0，PASS；69 Mod文件、70源码哈希项、6历史证据文件、47相对链接，无失败|logs/OP02-baseline.txt|
|`python tools/verify_manifest.py`|0，70项，failures=[]|logs/OP02-baseline.txt|
|`git show --no-patch --format=fuller HEAD`|0，固定提交及时间核对|logs/OP02-baseline.txt|
|`python ../review_source_inventory.py`|0；69文件、10,533,772字节、141,370行；未见括号失衡|logs/OP03-source-inventory.txt；source-inventory.json|
|`python ../review_verifier_fixtures.py`|0；6次原工具子进程，结果见下文|logs/OP04-verifier-fixtures.json|
|`python ../review_crosschecks.py`|0；25自定义scripted GUI定义、40处引用，无缺失；10本地化文件BOM/头正确，每文件无重复键；R76两文件哈希与历史candidate/after一致|logs/OP05-independent-crosschecks.json|
|`git status --porcelain=v1`|0，空输出|logs/OP05-independent-crosschecks.json|

读取/索引另外使用了 `rg --files`、`rg -n`、PowerShell带行号的 `Get-Content` 分段读取与 `Get-FileHash -Algorithm SHA256`。一次探索性 `rg` 把Windows通配符路径当成字面目录而退出1，后改用实际目录与 `-g` 完成；没有将这次退出1解释成源码问题。另有无匹配的 `rg` 退出1，属于搜索结果。

补充结构扫描只排除了注释和字符串再计数括号，不能验证CK3命令名、原生接口、DLC数据库、变量作用域、GUI绑定或引擎运行。扫描输出的重复 `on_game_start_after_lobby` 为两份回调注册，重复 `window` 是GUI节点；未据此认定冲突。扫描出的5个未定义候选经阅读是合约块的嵌套档位名，并非缺失脚本命令。

## 深入源码得到的现行链路

以下是读取固定提交实际文件形成的源码导航，不是游戏执行观察。

1. 自动维护从 `common/on_action/nhe19_on_actions.txt:2-12` 注册；标题/政体/封臣等入口经 `nhe19_process_lineage_effect` 或队列进入 `nhe19_deferred`（同文件124-129），再由 `nhe19_lifecycle.txt:197-209` 转到 `nhe45_process_effect`。开局扫描见 `nhe19_lifecycle.txt:212-220`，季度入口见on_actions的133-146。不是仅由旧PGH文档描述推定。
2. 自动创建入口位于 `nhe45_automatic.txt:17-30`，调用 `nhe19_create_effect`；后者在 `nhe19_lifecycle.txt:38-70` 创建county级载体、保存office→aux/dom及来源字段，并在79-87提交或保留失败结果。其适用入口是 `nhe19_triggers.txt:31-51`；见F3。
3. 自动合并的选择/执行在 `nhe45_automatic.txt:47-89`，源过滤在 `nhe45_triggers.txt:2-20`；`nhe19_triggers.txt:3-9,139-145`要求受标记的非世族county载体与来源住所对应。合并依次涉及 `nhe45_maa_fallback.txt`、`nhe45_resources.txt`、`nhe45_buildings.txt`，在 `nhe45_automatic.txt:116-126` 经过兵/余额/建筑检查后才发出销毁。可以从源码确认存在这些检查，不能从中声称原生引擎已实际执行或资产场景全通过。
4. 宫帐独立住所从 `zz_nhe19_steppe.txt:33` 指向 `nhe72_palace_estate`；独立类型 `zz_nhe72_palace_estate.txt:2-9`开启herd，普通类型 `zz_nhe19_estate.txt:2-8`未开启herd；共用类型识别在 `zz_nhe72_estate_types.txt:2-17`，初始化扩展在 `zz_nhe72_estate_setup.txt:71-96`。这能解释R72源码变化，但不证明旧住所自动改型。
5. 住所管理决议 `nhe47_md_decisions.txt:1-8` 调用context effect建列表，`nhe47_md_context_effects.txt:11-23,49`列出真实持有且有住所的头衔；`nhe47_md_manager.gui:59-81`以Title上下文传递selected_title到scripted GUI。确认交换经 `nhe47_md_guis.txt:60-71`→`nhe47_md_swap_building_effects.txt:10818-10844`→`events/nhe47_md_swap_events.txt:2-8`→`nhe47_md_sync_then_swap_effect`（core_effects:6590-6616）。准备、确认时检查和内核实际交换分属不同层。
6. 精确住所开窗通过 `nhe47_md_context_effects.txt:26-46`保存请求对象，再经 `nhe47_md_manager.gui:103-112` 的relay调用ToggleGameViewData并清请求。未把存在该绑定当作实际开窗成功。
7. 募兵确认按钮 `window_menatarms_type_view.gui:264-269`读取原生cost/can-create并调用原生Create。R59证据只能支持历史两次样本，不能由当前按钮代码推出全兵种付款正确。
8. R76中英文件均含住所类型别名，目标键在同文件存在；本次独立读取哈希分别为中文 `4d1a10440dc916ae139a10df6113560dc83ba554d15420b0728a18b9343bad24`、英文 `dfe8d068d3326590a2654e09bc95f63782bbfb911052a1aac02fcc76ff20716a`，与R76部署JSON的candidate/after相符。仅字节层通过，显示仍NOT_RUN。

## 按严重程度排列的可补缺口

### F1 [P2] 外置描述符可以被清单遗漏，错误安装路径仍获双PASS

位置：`tools/verify_handoff.py:32-42`，`tools/verify_manifest.py:6-12`；相关说明 `docs/HANDOFF.md:11`。

两个工具都逐项核验清单，但只对 `pgh_accounts/` 子树做actual/expected集合比较。外置 `pgh_accounts.mod` 虽在required中检查存在，却没有强制它必须在源码清单里，也没有核对path字段是否仍指向实际Mod目录。

独立复现：测试副本从source-manifest移除该描述符行，将其path改为 `mod/nonexistent-review-fixture`。两份未修改工具均exit0；handoff报告69源码项仍PASS。负对照只改源码一行而不改清单时，两工具正确exit1。

当前固定提交描述符确实在清单内且path正确，因此这是未来交接闸门漏检，不是当前安装包已损坏。

建议：校验清单结构、路径唯一/相对且位于仓库内；要求外置与内置描述符必需项；解析外置path确认对应当前 `pgh_accounts`，并检查必要描述字段一致。给这两个已复现输入加小型工具回归用例，保持CK3玩法源码不变。

### F2 [P2] 历史证据清单清空后核验仍PASS

位置：`tools/verify_handoff.py:51-55,81-85`，`docs/evidence/manifest.json:3-51`。

工具对 `evidence.get('files', [])` 循环，未要求非空、唯一、完整或与被声明的历史证据集合对应。在测试副本仅把files设为[]，handoff仍exit0/PASS，输出historical_evidence_files=0，虽然它已没有核验六份实际历史JSON的字节。

建议：验证manifest schema、files非空和路径唯一，检查本项目六份明确宣称的历史证据均被覆盖，拒绝清单漏项；以后增加或撤销证据时显式更新所宣称的集合与检查期望。哈希只证明保存字节一致，仍需保留历史结果不等于新测试的说明。

### F3 [P2] 安装文档缺少当前核心自动链的明确依赖和触发范围

位置：`docs/INSTALL.md:3-8`、`docs/HANDOFF.md:24`；源码依据 `pgh_accounts/common/scripted_triggers/nhe19_triggers.txt:31-51`、`common/governments/zz_nhe19_steppe.txt:131-133`。

文档说明复制、启用和版本边界，但只泛称要记录DLC列表。当前自动新建账户入口显式要求 `has_tgp_dlc_trigger` 和 `has_mpo_dlc_trigger` 同时成立，还要求存活宫帐政体、有地、大草原situation存在且下辖有相关county。首次安装者可能在该范围外等待自动创建，并误当成安装失败。住所管理器决议则是另一条较宽入口，不能把自动链条件泛化成全部功能的必要条件。

建议：只根据当前代码写一段“哪些核心功能要求TGP/MPO，以及自动创建在哪些角色/领地上触发”，链接源码。注明这是现存逻辑，不借文档补充擅自添加玩法门槛；其他DLC组合仍未经全面验证。

### F4 [P3] 历史运行摘录与当前源码的关联可更明确

位置：`docs/evidence/R59-payment.json:1-38`、`R74-creation.json:1-105`、`R74-restoration.json:17-25`，以及 `docs/evidence/README.md:3-10`。

R59记录游戏版本与两次付款样本，未记录被测源码树/关键文件哈希、实际加载Mod/DLC集合；R74创建摘录记录对象链，但未记录其被测源码/加载指纹或完整操作命令。R74恢复记录含存档与单GUI文件哈希，不能替代完整被测源码身份。证据manifest中的original_sha256是未上传原文件的指纹，不是源码加载证明。

README已经诚实说明这些限制，故不认定历史结果虚假，也不要求为了源码接手补跑游戏。

建议：如已有可公开的旧回执，补一份紧凑矩阵写清每次历史结果的被测源指纹、游戏版本、操作形态、观察范围、保留/未保留字段及与当前源码的已知差异。找不到的字段标UNKNOWN。若资料确实未保留，继续将历史绑定能力标PARTIAL；新的场景测试以后自行记录，不倒填历史。

## 仓库可以补齐与不能单靠仓库保证的事项

可以立即在仓库内完成：F1/F2工具约束及回归输入、F3依赖与作用范围说明、F4已有历史字段的可追溯性说明。也可以在SOURCE_MAP追加本报告确认的当前调用链导航；旧architecture已有醒目的归档提示，未发现应恢复旧计划的依据。

不能靠增加文档或重算哈希取得：当前反馈真实错误内容与来源身份；接手者的合法游戏与DLC环境；原生接口在其版本上的有效性；该机器实际加载的文件胜出、UI渲染、旧档迁移、完整原版决议点击、全部兵种/折扣/取消切换和第三方兼容场景。它们需要相应反馈或独立游戏环境及用户安排，保持NOT_RUN/UNKNOWN即可，不能算源码接手失败。

没有要求提供原作者机器路径、私有技能、原桥接环境或全部存档才能开始开发。当前可立即执行的下一步是保存固定提交身份、完善只读源码索引；获得当前脱敏反馈原文后，按 `docs/NEXT_STEPS.md:3-10` 将错误→具体版本/文件→入口→影响逐项关联，再考虑最小修复。现有仓库已足够让首次接手者知道这一点。

## 后续仅通过GitHub复核

获取新的远端完整SHA到另一个全新独立目录，不覆盖本次基线。复跑原工具，重放F1/F2夹具，检查F3文档与当前代码一致，检查F4仅增加真实已有字段且不提升运行状态。对比Mod文件与原始69文件及描述符哈希；如果本轮只修交接工具和文档，应能确认玩法源码未改。复核不读取主代理本地补丁或说明文件，只认新远端提交内容。

原始检出最终保持干净。所有审查产物位于本报告所在独立目录，`fixtures/` 是专门的异常输入副本，不能被当作开发候选或安装包。
