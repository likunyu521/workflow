# coding=UTF-8
#
# NOTE: Python 2 is deprecated in macOS, and has been removed from macOS 12.3+
#

import sys
from workflow import Workflow3
query = "{query}"
# query = "docx"

def query_result():

    docx = "https://feishu.cn/drive/create/?type=docx"
    doc = "https://feishu.cn/drive/create/?type=doc"
    sheet = "https://feishu.cn/drive/create/?type=sheet"
    bitable = "https://feishu.cn/drive/create/?type=bitable"
    mindnote = "https://feishu.cn/drive/create/?type=mindnote"

    rerult_list = {
        "doc":{'title': "新建文档",
               'subtitle': '' ,
               'valid': True,
               'arg': doc},
        "docx":{'title': "新建文档new",
                'subtitle': '' ,
                'valid': True,
                'arg': docx},
        "sheet":{'title': "新建表格",
                'subtitle': '' ,
                'valid': True,
                'arg': sheet},
        "bitable":{'title': "新建多维表格",
                'subtitle': '' ,
                'valid': True,
                'arg': bitable},
        "mindnote":{'title': "新建思维导图",
                'subtitle': '' ,
                'valid': True,
                'arg': mindnote}
    }
    wf = Workflow3()
    try:
        query_list = rerult_list[query]
    except Exception as e:
        query_list = ""
    # print(query_list)
    if query_list:
        wf.add_item(**query_list)
    else:
        for v in rerult_list.values():
            wf.add_item(**v)
    wf.send_feedback()

if __name__ == "__main__":
    query_result()
