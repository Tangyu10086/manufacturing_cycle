from clickhouse_driver import Client
import os

CH_HOST = os.getenv("CLICKHOUSE_HOST", "localhost")
CH_PORT = int(os.getenv("CLICKHOUSE_PORT", "9000"))
CH_USER = os.getenv("CLICKHOUSE_USER", "default")
CH_PASSWORD = os.getenv("CLICKHOUSE_PASSWORD", "123")

def init_database():
    client = Client(
        host=CH_HOST,
        port=CH_PORT,
        user=CH_USER,
        password=CH_PASSWORD,
    )

    try:
        client.execute("DROP TABLE IF EXISTS manufacturing_cycle")

        create_table_sql = """
        CREATE TABLE IF NOT EXISTS manufacturing_cycle (
            `zid` UInt64,
            `项目号` String,
            `项目简称` String,
            `项目名称` String,
            `车号` String,
            `节车号` String,
            `最早计划开始` Nullable(DateTime64(3)),
            `最晚计划结束` Nullable(DateTime64(3)),
            `进车计划开始` Nullable(DateTime64(3)),
            `Q30计划开始` Nullable(DateTime64(3)),
            `调车计划开始` Nullable(DateTime64(3)),
            `连接计划开始` Nullable(DateTime64(3)),
            `Q40计划开始` Nullable(DateTime64(3)),
            `发运计划开始` Nullable(DateTime64(3)),
            `进车实际开始` Nullable(DateTime64(3)),
            `Q30实际开始` Nullable(DateTime64(3)),
            `调车实际开始` Nullable(DateTime64(3)),
            `连接实际开始` Nullable(DateTime64(3)),
            `Q40实际开始` Nullable(DateTime64(3)),
            `发运实际开始` Nullable(DateTime64(3)),
            `组装周期天` Nullable(Float64),
            `落车周期天` Nullable(Float64),
            `调试周期天` Nullable(Float64),
            `交付周期天` Nullable(Float64),
            `整个制造周期天` Nullable(Float64)
        ) ENGINE = MergeTree
        ORDER BY zid
        """

        client.execute(create_table_sql)
        print("表 manufacturing_cycle 创建成功")

        sample_data = [
            {
                "zid": 1,
                "项目号": "B18B0301",
                "项目简称": "无锡4期",
                "项目名称": "无锡地铁4号线2期项目",
                "车号": "C001",
                "节车号": "A1",
                "最早计划开始": "2025-01-01 08:00:00",
                "最晚计划结束": "2025-03-31 18:00:00",
                "进车计划开始": "2025-01-10 08:00:00",
                "Q30计划开始": "2025-01-15 08:00:00",
                "调车计划开始": "2025-01-20 08:00:00",
                "连接计划开始": "2025-01-25 08:00:00",
                "Q40计划开始": "2025-02-01 08:00:00",
                "发运计划开始": "2025-02-10 08:00:00",
                "进车实际开始": "2025-01-10 09:30:00",
                "Q30实际开始": "2025-01-15 10:00:00",
                "调车实际开始": "2025-01-20 14:00:00",
                "连接实际开始": "2025-01-25 09:00:00",
                "Q40实际开始": "2025-02-01 11:00:00",
                "发运实际开始": "2025-02-10 08:30:00",
                "组装周期天": 5.2,
                "落车周期天": 4.8,
                "调试周期天": 7.5,
                "交付周期天": 9.0,
                "整个制造周期天": 26.5
            },
            {
                "zid": 2,
                "项目号": "B18B0301",
                "项目简称": "无锡4期",
                "项目名称": "无锡地铁4号线2期项目",
                "车号": "C001",
                "节车号": "B1",
                "最早计划开始": "2025-01-01 08:00:00",
                "最晚计划结束": "2025-03-31 18:00:00",
                "进车计划开始": "2025-01-12 08:00:00",
                "Q30计划开始": "2025-01-17 08:00:00",
                "调车计划开始": "2025-01-22 08:00:00",
                "连接计划开始": "2025-01-27 08:00:00",
                "Q40计划开始": "2025-02-03 08:00:00",
                "发运计划开始": "2025-02-12 08:00:00",
                "进车实际开始": "2025-01-12 08:00:00",
                "Q30实际开始": "2025-01-17 09:00:00",
                "调车实际开始": "2025-01-22 10:00:00",
                "连接实际开始": "2025-01-27 08:00:00",
                "Q40实际开始": "2025-02-03 09:00:00",
                "发运实际开始": "2025-02-12 10:00:00",
                "组装周期天": 5.0,
                "落车周期天": 5.0,
                "调试周期天": 7.0,
                "交付周期天": 9.0,
                "整个制造周期天": 26.0
            },
            {
                "zid": 3,
                "项目号": "S20S0101",
                "项目简称": "上海崇明",
                "项目名称": "上海崇明线项目",
                "车号": "C002",
                "节车号": "A1",
                "最早计划开始": "2025-02-01 08:00:00",
                "最晚计划结束": "2025-04-30 18:00:00",
                "进车计划开始": "2025-02-01 08:00:00",
                "Q30计划开始": "2025-02-05 08:00:00",
                "调车计划开始": "2025-02-10 08:00:00",
                "连接计划开始": "2025-02-15 08:00:00",
                "Q40计划开始": "2025-02-20 08:00:00",
                "发运计划开始": "2025-02-28 08:00:00",
                "进车实际开始": "2025-02-01 08:00:00",
                "Q30实际开始": "2025-02-05 08:00:00",
                "调车实际开始": "2025-02-10 11:00:00",
                "连接实际开始": "2025-02-15 09:00:00",
                "Q40实际开始": None,
                "发运实际开始": None,
                "组装周期天": 4.0,
                "落车周期天": 5.0,
                "调试周期天": 8.0,
                "交付周期天": None,
                "整个制造周期天": None
            },
        ]

        for data in sample_data:
            client.execute(
                """
                INSERT INTO manufacturing_cycle VALUES (
                    %(zid)s, %(项目号)s, %(项目简称)s, %(项目名称)s, %(车号)s, %(节车号)s,
                    %(最早计划开始)s, %(最晚计划结束)s,
                    %(进车计划开始)s, %(Q30计划开始)s, %(调车计划开始)s, %(连接计划开始)s, %(Q40计划开始)s, %(发运计划开始)s,
                    %(进车实际开始)s, %(Q30实际开始)s, %(调车实际开始)s, %(连接实际开始)s, %(Q40实际开始)s, %(发运实际开始)s,
                    %(组装周期天)s, %(落车周期天)s, %(调试周期天)s, %(交付周期天)s, %(整个制造周期天)s
                )
                """,
                data
            )

        print(f"成功插入 {len(sample_data)} 条示例数据")

        result = client.execute("SELECT `项目简称`, COUNT(*) FROM manufacturing_cycle GROUP BY `项目简称`")
        print("当前数据统计:")
        for row in result:
            print(f"  {row[0]}: {row[1]} 条记录")

    finally:
        client.disconnect()


if __name__ == "__main__":
    init_database()
