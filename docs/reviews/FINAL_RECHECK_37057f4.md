> 独立智能体最终复核，受审提交 `37057f4aea4608ad2f405c69f715033bb44d8bed`。本报告归档提交只更新报告/状态，不改已审工具或Mod源码。

# GitHub-only 最终独立接手复核报告：37057f4

审查仓库：https://github.com/apo-so/ck3-pgh-accounts

本次固定提交：`37057f4aea4608ad2f405c69f715033bb44d8bed`。

原始源码基线：`2adc0857ea961c89f091a95f996a57ed2b74c3ae`。

独立目录：`[INDEPENDENT_REVIEW_DIRECTORY]`。

## 最终结论

**源码接手 PASS；自动完整性闸门 PASS。** 本轮没有发现仍需在仓库内补齐的接手缺口。F1及其扩展R1、F2、F3已关闭；F4的说明缺口关闭，历史完整源码/加载绑定仍是PARTIAL边界。

|证据层次|最终结论|范围|
|---|---|---|
|只凭公开仓库开始源码开发与继续任务|PASS|有唯一入口、当前源码、状态、正确下一步、依赖与当前链路导航；无需作者私有工程或旧聊天。|
|当前快照完整性|PASS|69个Mod文件、70项源码哈希、6份历史证据和74相对文档链接通过原核验；本次解压106文件均与远端ZIP一致。|
|自动完整性闸门|PASS|仓库13回归、独立10整仓样本和11词法边界对照均符合预期。这里只评价仓库完整性、描述符和已审查输入边界，不是CK3语义编译器。|
|71保护文件保持原始字节|PASS|69 Mod文件、外置描述符、source-manifest与新下载的2adc085基线全部逐字节一致。|
|历史说明及结果摘录可读性|PASS|矩阵按实际字段标明R59/R72/R74/R76各自范围与UNKNOWN，不把旧结果当新测试。|
|历史全部被测源码与加载身份绑定|PARTIAL|R59/R74缺少当时完整源码指纹与加载环境；R76仅能绑定两份当前本地化字节。|
|新机器部署、实际加载、游戏行为、渲染、用户验收|NOT_RUN|本轮没有读取安装目录，也没有部署、启动或控制游戏。|

## 初审与复核问题闭环

|问题|最终状态|独立取得的证据|
|---|---|---|
|F1 外置描述符清单漏项、错误path|CLOSED|原F1复现稳定双exit1；必需条目和实际path检查有效。|
|R1 同一行第二path/版本字段漏计|CLOSED|两个原样输入稳定双exit1；新词法读取统计根级键赋值，未依赖行边界。合法单行字段、注释/字符串伪字段、转义引号等正对照仍能通过。|
|F2 空历史证据清单|CLOSED|原F2复现verify_handoff exit1；仓库回归还覆盖必需证据丢失。仅查源码的verify_manifest在此场景exit0符合职责。|
|F3 自动新建账户路径依赖与适用范围|CLOSED|INSTALL:10-16与当前nhe19_triggers:31-51一致，明确TGP/MPO及宫帐/有地/大草原条件，并限定只是该自动路径。|
|F4 历史证据与当前源码关系不清|BOUNDARY，说明缺口CLOSED|TRACEABILITY:3-13说明被测身份缺失和R76两文件绑定，没有补猜旧字段；完整历史绑定保留PARTIAL。|

关闭的是仓库内能修的工具与说明问题。未取得的原生存档、历史完整加载身份、当前反馈原文或新游戏场景结果，没有通过文档或哈希被“关闭”。

## 独立获取与隔离

本轮使用另一全新目录。所有项目材料均从GitHub固定SHA的公开HTTPS归档和只读GitHub compare API取得，没有读取主代理本地补丁、私有工程、安装目录、记忆或其他本地仓库。仓库内上传的初审/复核报告与“已修复”说明仅作为被审资料，没有当作本次通过证据。

新提交下载URL：`https://codeload.github.com/apo-so/ck3-pgh-accounts/zip/37057f4aea4608ad2f405c69f715033bb44d8bed`。

基线下载URL：`https://codeload.github.com/apo-so/ck3-pgh-accounts/zip/2adc0857ea961c89f091a95f996a57ed2b74c3ae`。

两次均使用 `Invoke-WebRequest -Uri <固定SHA URL> -OutFile <独立目录对应ZIP> -TimeoutSec 60`，随后 `Expand-Archive -LiteralPath <ZIP> -DestinationPath <独立提取目录>`。两次下载、解压命令均exit0。本轮未使用Git clone，因此不声称有Git checkout；归档取自固定完整SHA，并由GitHub只读compare记录相互核对。

新归档SHA256：`33ac2253115df3933bf96dce2988bbb03b1c3c2e3dee1a0f3fcfac14a818b7b6`。

基线归档SHA256：`553cf10ad489192acb0a64929c8605a6f70d2a0d1bd38a895b9fc27d1ce22f0d`。

实际被审目录：`new-archive/ck3-pgh-accounts-37057f4aea4608ad2f405c69f715033bb44d8bed/`。原始基线也在本轮新下载的 `baseline-archive/` 中。

只读GitHub compare API确认两次提交之间只有交接工具/文档/状态的16个文件变化；不含pgh_accounts、pgh_accounts.mod或source-manifest.json。原始API响应见 `logs/OP01-remote-compare.json`。另外用实际下载的两个归档逐项计算SHA256，不仅依赖API文件列表。

## 实际执行命令和退出码

环境：PowerShell、Python 3.13.3；没有安装第三方Python依赖。首先完整阅读了本轮project_checks、两个核验入口、test_integrity及现行接手/安装/证据文档，再执行工具。

前三项工作目录为本轮被审归档目录：

|实际命令|退出码|结果|
|---|---:|---|
|`python --version`|0|Python 3.13.3|
|`python tools/verify_handoff.py`|0|PASS，69 Mod文件、70源码项、6历史证据文件、74相对链接、failures=[]|
|`python tools/verify_manifest.py`|0|70源码项、69 Mod文件、failures=[]|
|`python tools/test_integrity.py`|0|13/13场景PASS|
|`python <独立目录>/independent_final_recheck.py`|0|10整仓样本、11词法对照全部PASS；71保护文件无差异|
|`python <独立目录>/final_integrity.py` 初次|1|审查者附加出处核对脚本误把两种provenance字段名当成同名；已保留首次脚本/输出，并修正映射。这是审查脚本错误，不是仓库哈希差异。|
|同一附加出处核对脚本，修正字段映射后|0|106解压文件无漂移；两份上传审查报告的脱敏哈希及原始出处指纹一致；R76两文件当前绑定一致。|

首次附加出处检查读取RECHECK记录时用了 `report_sanitized_sha256`，实际该记录字段为 `sanitized_report_sha256`。实际哈希与正确字段从一开始就相等。保存了 `final_integrity.initial.py`、`logs/OP04-first-attempt.json` 和首次失败输出；修正只发生在审查者目录，未改被审仓库，也没有重跑不受影响的源码/工具回归。

## 独立故障重放与正负对照

整仓夹具均复制到审查目录 `fixtures/`，修改后按需要只更新夹具自身描述符清单哈希，再调用未经修改的本轮工具。以下两列顺序为verify_manifest、verify_handoff：

|独立整仓样本|预期退出码|实际退出码|
|---|---|---|
|原F1：删外置描述符清单项，path改为不存在目录|(1,1)|(1,1)|
|原F2：历史evidence.files=[]|(0,1)|(0,1)|
|R1原样：追加 `tags={} path="mod/nonexistent-review-fixture"`|(1,1)|(1,1)|
|R1原样：追加 `tags={} supported_version="0.0.*"`|(1,1)|(1,1)|
|合法全部根字段放同一行|(0,0)|(0,0)|
|注释与标签字符串内含伪path、版本、#及花括号|(0,0)|(0,0)|
|标签字符串含转义引号、#和花括号|(0,0)|(0,0)|
|未闭合字符串|(1,1)|(1,1)|
|未闭合标签块|(1,1)|(1,1)|
|带引号根键形式追加第二path|(1,1)|(1,1)|

20个工具子进程均达到预期，无stderr。原始完整stdout/退出码保存在 `logs/OP03-independent-fixtures.json`，不是仅记录一个汇总PASS。

另外直接调用下载源码中的descriptor_fields，保存了11个具体输入和完整返回值/异常：合法单行根字段、注释/字符串中的伪键、转义引号与嵌套花括号、带引号的重复根键、紧接块末尾的重复键，以及未闭引号、未闭块、缺值、多余右括号、缺等号、孤立token。全部符合预期，见 `logs/OP03-lexer-controls.json`。这些只验证描述符读取的词法边界，不宣称Launcher或引擎已经运行接受任意新输入。

本轮仓库自身13项回归也独立执行：正常副本、源码漂移、描述符漏项、错误路径重算哈希、元数据不一致重算哈希、两项同行重复字段、注释/字符串正对照、合法同行字段、空证据、必需证据丢失、重复源码项和非法结构。完整结果见 `logs/OP02-repository-regression.json`。

## 源码字节与历史边界

新旧远端归档各69个Mod文件，合计71个保护文件逐项SHA一致，文件集合未改变。完整新旧哈希保存在 `logs/OP03-byte-comparison.json`。因此初审已经追踪的现行源码链、GUI脚本引用、本地化结构没有被这两轮工具/文档修复改动；没有重复未受影响的初审结构检查。

复核结束时，全部106个被审文件与新下载ZIP一致，`extracted_drift=[]`。异常夹具是独立副本，不是开发候选或安装包。

R76当前中文文件SHA为 `4d1a10440dc916ae139a10df6113560dc83ba554d15420b0728a18b9343bad24`，英文为 `dfe8d068d3326590a2654e09bc95f63782bbfb911052a1aac02fcc76ff20716a`，均与已提供历史candidate/after值一致。但两文件新进程加载与实际名称显示仍NOT_RUN。

R59/R74无法从摘录补造当时完整源码身份、Mod/DLC加载集合或原生存档。源码接手与自动闸门通过，不提升这一历史绑定能力，也不构成任何本次游戏PASS。

## 交付与下一步

本次完成独立GitHub-only源码接手审查闭环，没有待补的仓库内问题，也没有未结束的下载或测试进程。保存范围包括计划、所有审查脚本、原始核验/回归/夹具输出、71文件比较、API响应和最终完整性核查。

后续开发可以从当前仓库独立分支开始，先依NEXT_STEPS核对实际反馈所用版本和脱敏错误原文，逐项归因后制作最小修复。当前反馈未提供的状态不阻止源码接手，但实际报错复现和游戏测试需相应反馈/环境及用户安排；本次不自动扩大成游戏运行或部署。
