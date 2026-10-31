> 第一轮复核历史报告，针对提交 `e2987c920fdb0cfcbe2ee03e0ef33569b6eeada6`；发现的R1仍需下一提交处理。最新状态见 [审查闭环](README.md)。

# GitHub-only 独立复核报告：e2987c9

目标仓库：https://github.com/apo-so/ck3-pgh-accounts

本次固定提交：`e2987c920fdb0cfcbe2ee03e0ef33569b6eeada6`。

远端基线：`2adc0857ea961c89f091a95f996a57ed2b74c3ae`。

独立目录：`[INDEPENDENT_RECHECK_DIRECTORY]`。

## 分层结论

|项目|结论|本次独立依据|
|---|---|---|
|源码接手|PASS|入口、状态、下一步、当前链路与历史边界可以只靠仓库理解；69个Mod文件完整。|
|当前原始快照完整性|PASS|两个原仓库核验入口均exit0；解压后的104文件与远端ZIP逐项SHA256相同。|
|自动完整性闸门|PARTIAL|原F1/F2复现已拦截；扩展描述符同一行重复字段仍漏检，见R1。|
|与原始源码的字节一致性|PASS|69个Mod文件、外置描述符和源码清单共71文件与远端2adc085全部相同。|
|历史证据可追溯说明|PASS_LIMITED|新增矩阵按实际JSON字段标明能绑定的范围和UNKNOWN，未冒充重新测试。|
|历史全部被测源码/加载绑定|PARTIAL / BOUNDARY|R59/R74缺失的原始加载身份并未因本次文档改动取得；R76仅可绑定两文件字节。|
|新机器部署、实际加载、游戏场景、渲染、用户验收|NOT_RUN|本复核没有访问安装目录或启动/控制游戏。|

## F1—F4逐项结论

|初审项|本次状态|说明|
|---|---|---|
|F1 描述符漏项与错误path|OPEN（原复现已CLOSED，扩展同类问题仍OPEN）|必需条目和独占行错误path已被拦截；但按行正则会漏计同一行中的第二个根级赋值。|
|F2 空历史证据清单|CLOSED|独立将files清空后，handoff稳定exit1；仓库回归也验证必需证据丢失被拒绝。verify_manifest只查源码，对证据变异exit0符合职责。|
|F3 自动链依赖与触发范围缺失|CLOSED|INSTALL:10-16明确TGP/MPO和宫帐/有地/大草原范围，并限定只是自动创建路径；与nhe19_triggers:31-51一致，没有新增玩法条件。|
|F4 历史证据和当前源码关系|BOUNDARY（说明缺口已CLOSED）|TRACEABILITY:3-13逐项说明R72/R59/R74/R76绑定强度和缺失字段。不能以增加矩阵补造旧原始证据；历史完整绑定仍PARTIAL。|

## 实际获取方式

所有项目文件均来自GitHub远端，本次未读取主代理本地修改、工程、补丁、安装目录或任何记忆。上传的初审报告与修复说明是被审资料；本报告结论来自重新下载、执行和异常输入试验。

最初在新建 `repository/` 内执行 `git init`、`git remote add origin https://github.com/apo-so/ck3-pgh-accounts.git`、`git fetch --depth 1 origin e2987c920fdb0cfcbe2ee03e0ef33569b6eeada6`。fetch长时间无输出，已通过仅该exec会话7471的中断结束，exit1；没有成功checkout，不声称Git检出完成。

随后使用固定SHA的公开HTTPS codeload ZIP成功获取两个提交：

```powershell
Invoke-WebRequest -Uri 'https://codeload.github.com/apo-so/ck3-pgh-accounts/zip/e2987c920fdb0cfcbe2ee03e0ef33569b6eeada6' -OutFile <独立目录>/e2987c9.zip -TimeoutSec 60
Expand-Archive -LiteralPath <独立目录>/e2987c9.zip -DestinationPath <独立目录>/archives
Invoke-WebRequest -Uri 'https://codeload.github.com/apo-so/ck3-pgh-accounts/zip/2adc0857ea961c89f091a95f996a57ed2b74c3ae' -OutFile <独立目录>/2adc085.zip -TimeoutSec 60
Expand-Archive -LiteralPath <独立目录>/2adc085.zip -DestinationPath <独立目录>/archives
```

归档下载和解压命令均exit0。新归档SHA256：`c323da4e6fe452e64486a6b6cea7dadf15272ecb17b44eea4033c99e6ad3970f`；基线归档SHA256：`553cf10ad489192acb0a64929c8605a6f70d2a0d1bd38a895b9fc27d1ce22f0d`。ZIP归档自身不是源码树SHA，但按SHA固定的远端URL、GitHub提交页面和只读compare API互相对应。

实际被审目录为 `archives/ck3-pgh-accounts-e2987c920fdb0cfcbe2ee03e0ef33569b6eeada6/`。基线目录也仅为本次从GitHub新下载的归档，不依赖初审本地clone。

另通过GitHub连接器只读GET compare端点 `https://api.github.com/repos/apo-so/ck3-pgh-accounts/compare/2adc0857ea961c89f091a95f996a57ed2b74c3ae...e2987c920fdb0cfcbe2ee03e0ef33569b6eeada6`，返回ahead_by=1、目标commit=e2987c9、仅14文件变化，未包含任何pgh_accounts源码、外置描述符或source-manifest。完整响应存于 `logs/OP03-remote-comparison.json`。

## 实际命令与退出码

环境：PowerShell、Python 3.13.3；未安装第三方Python包。

以下仓库命令工作目录为上述新归档目录：

|命令|退出码|实际结果|
|---|---:|---|
|`python --version`|0|Python 3.13.3|
|`python tools/verify_handoff.py`|0|PASS，69 Mod文件、70源码项、6证据文件、72相对链接，failures=[]|
|`python tools/verify_manifest.py`|0|70项、69 Mod文件，failures=[]|
|`python tools/test_integrity.py`|0|9/9场景PASS；包括baseline、源码漂移、描述符漏项、重算哈希后的错误path/元数据、空证据、必需证据丢失、重复源码项、非法结构。|
|`python <独立目录>/independent_recheck.py`|0|远端双归档71保护文件逐字节一致；另在私有fixtures复制目录执行10次未修改工具子进程。|
|`python <独立目录>/final_crosschecks.py`|0|104实际文件与ZIP无漂移；初审脱敏报告哈希匹配provenance；R76当前字节绑定仍一致。|

原始输出：`logs/OP02-baseline.txt`、`OP02-repository-regression.json`、`OP03-independent-recheck.txt`、`OP03-independent-fixtures.json`、`OP04-final-integrity.json`。OP04文本日志内中文片段有宿主标准输出编码显示问题；实际UTF-8文件可严格解码，JSON哈希结果和远端字节比较未受影响，未将其认定为仓库乱码。

独立异常输入与子进程结果：

|夹具|verify_manifest退出码|verify_handoff退出码|判断|
|---|---:|---:|---|
|源码加注释且不更新哈希|1|1|负对照正确失败|
|重放原F1：清单删外置描述符，path改不存在目录|1|1|原漏洞关闭|
|重放原F2：evidence.files=[]|0|1|handoff正确失败|
|原描述符末尾追加同一行第二path，更新描述符清单哈希|0|0|新同类漏洞复现|
|原描述符末尾追加同一行第二supported_version，更新清单哈希|0|0|新同类漏洞复现|

## R1 [P2] 描述符字段解析依赖独占行，漏计同一行中的重复赋值

文件/行：`tools/project_checks.py:69-71,76-82`；目前仓库回归 `tools/test_integrity.py:38-47` 只覆盖直接替换规范行，未覆盖同行重复字段。

实际复现均仅修改独立测试副本，未更改被审归档。保留原外置描述符的全部正常行，在末尾追加：

```text
tags={} path="mod/nonexistent-review-fixture"
```

随后只把source-manifest中该外置描述符的SHA更新为真实新哈希。文件内存在第二个path赋值，但现行正则只识别从行首到行尾独占的path，漏计该行中的path；两个核验入口均exit0，handoff仍PASS。

将追加行换为以下内容也同样双exit0：

```text
tags={} supported_version="0.0.*"
```

这证明核验器的“exactly path”和“duplicated metadata”检查不能覆盖普通空白分隔的根级赋值。本复核没有运行Launcher/CK3，因此不声称引擎最终采纳哪一个重复值；无需该运行断言即可确认工具未计出文件中的第二个字段。

建议：用能忽略注释并识别引号/花括号的最小词法扫描，统计根级键赋值，字段边界按token而非换行；或明确执行严格规范格式并拒绝任何未解析的非空语句。将上述两个同一行重复字段输入纳入回归，保留现有原F1/F2测试和源码未改的边界。

已及时把完整复现发给主代理；主代理表示将准备下一提交。本报告仍只评价e2987c9，没有读取或认可未上传修复。

## 历史证据和文档核查

新增INSTALL描述与源码的 `nhe19_governor_trigger`、`nhe46_steppe_realm_trigger`、`nhe19_new_office_trigger` 一致；没有把自动创建条件扩成所有界面的共同门槛。

TRACEABILITY明确：R59缺少被测源码和加载集合；R74游戏版本和加载指纹UNKNOWN，完整原生决议点击未测；R72静态审计未提供完整被测树指纹；R76当前两语言文件candidate/after哈希一致，但新进程加载和显示未测。文档保持这些边界，未把UNKNOWN改成PASS。

当前R76中文哈希 `4d1a10440dc916ae139a10df6113560dc83ba554d15420b0728a18b9343bad24`，英文 `dfe8d068d3326590a2654e09bc95f63782bbfb911052a1aac02fcc76ff20716a`，均与已提供R76部署摘录一致。

被审初审脱敏报告实际SHA256为 `bb6a52f1bc5c4c8cf6e927c411458a91dfc2465b5203c0101ffe27cb20a40497`，匹配上传provenance；其original_sha256也匹配本代理初审形成的指纹。这只核对文档出处，不代替本次复核工具输出。

## 原始源码保护与下一步

双归档独立计算确认：两个提交各69个Mod文件；69文件加外置描述符与source-manifest共71项，无一字节改变。全部变化只有14项工具/文档/状态文件，与GitHub compare API一致。详尽71项新旧哈希保存在 `logs/OP03-byte-comparison.json`。

全部被审104文件在复核后仍与远端ZIP逐字节相同。异常输入均留在 `fixtures/`，不能当开发候选或安装包。没有部署、游戏运行、私有工程读取或未结束的下载/测试进程。

下一步：仅接收新的远端完整SHA，在第三个全新目录取得提交；复跑两个核验入口及仓库回归，重放R1两种同行重复字段，同时保留F1/F2原异常输入。若词法修复引入新行为，则只对受影响解析边界做相称检查。源码接手已经PASS；工具同类漏洞修好前自动闸门保持PARTIAL。游戏和历史原始材料边界不因工具补齐而升级。
