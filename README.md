# xixi.aistar.cool

西西Claire 的个人主页静态站。

## 站点定位

用于聚合以下内容：
- 精选项目
- AI见闻
- AI精选项目
- AI高质量中转
- AI代充（Claude 代充 / ChatGPT 代充）

## 本地开发

```bash
python3 -m http.server 8000
```

打开：
- http://127.0.0.1:8000/

## 校验

```bash
python3 tests/verify_homepage_card.py
```

## 部署目录

生产目录：
- `/www/wwwroot/xixi.aistar.cool`

当前首版部署通过 SSH 直传到服务器目录完成，因为初始化时提供的 FTP 凭据未能登录。
后续如果 FTP 修复，也可恢复 FTP 发布。

## 缓存刷新

修改以下资源时，要同步更新 `index.html` 中的版本号查询参数：
- `css/style.css?v=...`
- `js/main.js?v=...`
- `public/avatar.svg?v=...`
- `public/favicon.svg?v=...`
