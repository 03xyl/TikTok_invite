import datetime
from pathlib import Path

import pandas as pd
from loguru import logger


# 切割xlsx文件
def split_xlsx(file_path: str, index: int = 0) -> list:
    df = pd.read_excel(file_path)
    # 转化为列表
    data_list = df.values.tolist()
    data_list = [data[0] for data in data_list if int(data[-1]) == 1]
    # 写入xlsx文件,只需要前20行
    flag = len(data_list)
    flag = flag - 1 if flag % 20 == 0 else flag // 20
    if index <= flag:
        # 表头需要自己添加
        names = data_list[:20]
        df = pd.DataFrame(names, columns=['达人用户名'])
        df.to_excel('creator_template.xlsx', index=False)
        # update_status(names)
        return [True, names]
    else:
        return [False]


def update_status(names: list[str]) -> None:
    """
    将使用过的达人状态修改为0
    :return: None
    """
    try:
        path = str(Path(__file__).resolve().parent /'TKPersonData.xlsx')
        # 读取Excel文件
        df = pd.read_excel(path)
        # 通过name来修改状态
        for name in names:
            df.loc[df['name'] == name, ['status', 'updated_time']] = 0, pd.to_datetime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        # 保存修改
        df.to_excel(path, index=False)
    except Exception as e:
        logger.error(f'修改状态失败，错误原因：{e}')


# with open('./user_pwd.txt', 'r', encoding='utf-8') as f:
#     names = f.read().strip().split('\n')
# update_status(["603nicoleannlavoie"])
