import akshare as ak  # 1.12.95
import pandas as pd  # 2.2.1


def test(code):
    stock_qfq_df = ak.stock_zh_a_hist(symbol=code, adjust="qfq").iloc[:, :6]
    # 处理字段命名，以符合 Backtrader 的要求
    stock_qfq_df.columns = [
        'date',
        'open',
        'close',
        'high',
        'low',
        'volume',
    ]
    # 把 date 作为日期索引，以符合 Backtrader 的要求
    stock_qfq_df.index = pd.to_datetime(stock_qfq_df['date'])
    print(stock_qfq_df)


if __name__ == "__main__":
    test("002594")
