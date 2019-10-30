## 插件简介

|插件|状态|简单的说明|
|----------------------------|:-:|---
|AdvancedNewFile             |   |快速创建文件
|ChineseLocalizations        | √ |ST菜单本地化
|ChineseOpenConvert          |   |繁简中文转换
|Codecs33                    | √ |ConvertToUTF8插件依赖
|Compare Side-By-Side        | √ |简单的文件差异比较
|ConvertToUTF8               | √ |打开 GB2312, GBK, BIG5, EUC-KR, EUC-JP编码文档，解决乱码
|DiffTabs                    | √ |文件差异比较
|HaoGist                     | √ |Gist 插件
|HTML-CSS-JS Prettify        |   |html/css/js格式化（依赖node.js）
|Inline Google Translate     |   |文档内google翻译插件
|LaTeXTools                  |   |Latex插件
|Local History               | √ |本地自动备份
|Markdown Extended           | √ |YAML Front Matter、GFM“围栏”代码块高亮，扩展默认主题 Monokai
|MarkdownEditing             |   |功能强大的Markdown软件包，具有更好的语法理解和良好的配色方案。
|Markdown​Preview             |   |Markdown​预览插件
|Mermaid                     |   |mermaid解析及预览
|OmniMarkupPreviewer         | √ |md等预览插件
|Package Control             | √ |Package Control核心插件
|PackageResourceViewer       |   |ST 插件包内资源查看
|Side-by-Side Settings       | √ |在新窗口中并排查看默认和用户设置，支持键绑定和插件特定。
|SideBarEnhancements         | √ |ST 侧边栏增强。文件和文件夹
|SublimeTmpl                 | √ |模板插件
|Sync Settings               | √ |ST 个人设置双向同步到Gist
|Terminus                    | √ |终端内嵌插件
|TrailingSpaces              | √ |高亮显示多余的空格和Tab，并可一键删除
|[CustomizeMarkdownEditor](https://github.com/maboloshi/CustomizeMarkdownEditor)     | √ |打开自定义 Markdown 编辑器(OSX)[自己改造的插件]

## 其他设置文件
### SyncSettings.sublime-settings
```json
{
    "access_token": "<personal access token>",
    // 忽略列表
    // 注意: 需要*打头, 才可能有效
    "excluded_files":
    [
        "*.git/*",
        "*HaoGist.sublime-settings",
        "*.nosync",
        "*.nosync/*",
        "*HaoGist/*",
        "*~",
        "*~.sublime-*",
        "*encoding_cache.json",
        "*.dmg",
        "*.DS_Store*",
        "*.Spotlight-V100",
        "*.Trashes",
        "*oscrypto-ca-bundle*.crt",
        "*Package Control*.last-run",
        "*Package Control*.ca-list",
        "*Package Control*.ca-bundle",
        "*Package Control.cache/*",
        "*Package Control.ca-certs/*",
        "*Package Control*.merged-ca-bundle",
        "*Package Control*.system-ca-bundle",
        "*Package Control*.user-ca-bundle",
        "*SBSCompareScheme*.hidden-color-scheme",
        "*.exe",
        "*Thumbs.db",
        "*ehthumbs.db"
    ],
    "gist_id": "<gist_id>",
    // 包含列表
    "included_files":
    [
    ]
}
```

### HaoGist.sublime-settings
```json
{
    // Gist token
    "token": "<personal access token>",
    // Update gist on save
    // If true, open command palette → “HaoGist: Open Gist From Cache” → select, edit and save your gist → your changes apply to remote gist.
    "auto_update_on_save": false,
}
```

点击创建 [私人访问令牌](https://github.com/settings/tokens/new?scopes=gist,&description=SublimeText+2/3+Gist,Sync+plugin) 替换`<personal access token>`。

### 安装其他插件自定义菜单
```sh
User_path=~/Library/Mobile\ Documents/com\~apple\~CloudDocs/设置/Sublime/User/
Packages_path=~/Library/Application\ Support/Sublime\ Text\ 3/Packages/

# SideBarEnhancements菜单
mkdir -p $Packages_path/SideBarEnhancements/
ln -s $User_path/SideBarEnhancements/Side\ Bar.sublime_menu $Packages_path/SideBarEnhancements/Side\ Bar.sublime-menu

```
> 此处`<User_path>`、`<Packages_path>`为示例，请根据自身情况修改。