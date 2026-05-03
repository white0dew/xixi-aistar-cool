# xixi.aistar.cool 维护约定

## 项目概览
- 域名：`xixi.aistar.cool`
- 类型：传统静态站（HTML + CSS + JS）
- 服务器：香港服务器 `103.38.82.9`
- 线上目录：`/www/wwwroot/xixi.aistar.cool`
- Web 环境：宝塔面板 + nginx

## 页面核心内容
- 人物名：`西西Claire`
- 副标题：`AI产品 / vibe coding / marketing`
- 首页入口：
  - 精选项目
  - AI见闻
  - AI精选项目
  - AI高质量中转
  - AI代充
- AI代充区块需保留：
  - Claude 代充
  - ChatGPT 代充
- 联系方式：
  - 小红书：`西西碎碎念`
  - 微信：`CindyW2020`
  - 所在城市：`成都`

## 资源版本号
只要修改下面任一资源内容，必须同步更新 `index.html` 中的查询参数版本号：
- `css/style.css?v=...`
- `js/main.js?v=...`
- `public/avatar.svg?v=...`
- `public/favicon.svg?v=...`

推荐格式：`YYYYMMDD-N`

## 发布建议
优先用 SSH / rsync / scp 直传到：
- `/www/wwwroot/xixi.aistar.cool`

原因：首版初始化时，FTP 凭据登录失败；但服务器目录、nginx vhost、HTTP 站点已就绪。

## 验证步骤
1. 运行：`python3 tests/verify_homepage_card.py`
2. 本地起服务：`python3 -m http.server 8000`
3. 浏览器检查首页与代充区块
4. 发布到服务器目录
5. 服务器侧用 Host 头验证：
   - `curl -I -H 'Host: xixi.aistar.cool' http://127.0.0.1/`
6. 如果公网 DNS 未生效，可先用 `--resolve` 或本地 hosts 方式验证

## 当前已知事实
- 线上根目录已存在，默认内容曾是宝塔成功页
- `xixi.aistar.cool` 的 nginx 站点配置已存在并指向 `/www/wwwroot/xixi.aistar.cool`
- 当前公网 DNS 还未解析到该服务器
- 当前未见 `xixi.aistar.cool` 的 SSL 证书与 443 配置
