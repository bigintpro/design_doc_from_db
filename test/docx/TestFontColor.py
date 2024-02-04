

from docx import Document
from docx.shared import RGBColor

if __name__ == '__main__':

    # 创建一个新的Word文档
    doc = Document()

    # 添加一个段落
    paragraph = doc.add_paragraph()

    # 添加文本内容
    run = paragraph.add_run("Hello, World!")

    # 设置字体颜色为红色
    font = run.font
    font.color.rgb = RGBColor(255, 0, 0)

    # 保存文档
    doc.save("font_color.docx")
