# 修订稿的源文件与构建脚本

`src/` 下是修订稿的纯文本源文件，按章节拆分；`.docx` 由它们生成。以后要改正文，改这里的文本再重新构建即可，Word 文件里的样式、目录和页码会自动保持一致。

标记约定：`#` 一级标题，`##` 二级标题，`>` 古文引文，`**粗体**`，`*斜体*`，`|` 开头的行是表格，`@ref` 是参考文献条目，`@pagebreak` 分页。

构建需要 Node.js 的 `docx` 包、LibreOffice（用于计算目录页码）与 poppler-utils：

```bash
npm install docx
./make.sh /path/to/output.docx
```

`make.sh` 先生成文档，再用 LibreOffice 渲染一遍，取得各标题所在页码，写回目录域的缓存值，最后复查页码是否稳定。脚本中的临时目录写死为 `/tmp/lotest`，换环境时按需修改。
