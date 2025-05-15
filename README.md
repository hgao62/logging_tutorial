# Python Logging 教程示例

本项目演示了如何在 Python 项目中使用标准库 `logging` 进行日志记录。

## 目录结构

```
logging_tutorial/
├── main.py
├── transform.py
├── app.log
```

## 主要内容

- 如何配置日志格式、日志级别和日志文件
- 如何在代码中记录不同级别的日志（DEBUG, INFO, WARNING, ERROR, CRITICAL）
- 如何在函数调用和异常处理中记录日志

## 快速开始

1. **安装 Python**

   确保你已安装 Python 3.x。

2. **运行示例代码**

   在命令行中运行：

   ```powershell
   python main.py
   ```

3. **查看日志输出**

   日志会被写入到 `app.log` 文件中。你可以用文本编辑器打开查看。

## 代码说明

### 日志配置

在 `main.py` 中，使用如下方式配置日志：

```python
logging.basicConfig(
    filemode="a", # 追加模式
    format="%(asctime)s - %(levelname)s- %(filename)s:%(lineno)s  - %(message)s", # 日志格式
    filename="app.log", # 日志文件名
    level=logging.INFO, # 日志级别
)
logger = logging.getLogger(__name__)
```

### 日志记录示例

```python
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
```

### 异常日志

主函数被 try/except 包裹，异常会被记录到日志：

```python
try:
    main()
except Exception as e:
    logger.error("An error occurred: %s", e, exc_info=True)
    raise
```

## 进阶用法

- 可以在 `transform.py` 里也引入 logger，实现模块级日志。
- 可调整 `level` 为 `DEBUG` 以输出更多调试信息。

## 参考

- [Python 官方 logging 文档](https://docs.python.org/zh-cn/3/library/logging.html)
