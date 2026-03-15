---
title: 贡献指南
icon: hand-holding-heart
order: 2
---

# 贡献指南

欢迎为 Pyisland 项目贡献代码！本指南将帮助你了解如何参与项目开发。

## 开发环境设置

### 1. 克隆仓库

```bash
git clone https://github.com/Python-island/Python-island.git
cd Python-island
```

### 2. 创建开发分支

```bash
# 基于主分支创建新分支
git checkout -b feature/your-feature-name
# 或基于 pyislandPyside6 分支
git checkout -b feature/your-feature-name pyislandPyside6
```

### 3. 设置预提交钩子（可选）

项目使用 pre-commit 钩子确保代码质量：

```bash
pip install pre-commit
pre-commit install
```

## 代码规范

### Python 代码风格

- 遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 规范
- 使用 4 空格缩进
- 使用类型注解（Type Hints）
- 保持函数简洁，单一职责

### 命名规范

| 类型 | 命名方式 | 示例 |
|------|----------|------|
| 类名 | PascalCase | `class IslandWindow` |
| 函数名 | snake_case | `def get_brightness()` |
| 常量 | UPPER_SNAKE_CASE | `DEFAULT_WIDTH = 300` |
| 私有方法 | _snake_case | `def _update_status()` |

### 文档字符串

使用 Google 风格的文档字符串：

```python
def get_brightness() -> int:
    """获取当前系统亮度百分比。

    Returns:
        int: 亮度百分比 (0-100)

    Raises:
        BrightnessError: 获取亮度失败时抛出
    """
    pass
```

## 提交规范

### 提交信息格式

```
<类型>(<范围>): <描述>

[可选的正文]

[可选的脚注]
```

类型包括：
- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式调整
- `refactor`: 代码重构
- `perf`: 性能优化
- `test`: 测试相关
- `chore`: 其他更改

示例：

```
feat(brightness): 添加亮度调节防抖功能

添加了 180ms 的防抖机制，避免频繁调节系统亮度

Closes #123
```

## 提交 Pull Request

### 1. 推送分支

```bash
git push origin feature/your-feature-name
```

### 2. 创建 PR

在 GitHub 上创建 Pull Request，包含：

- **标题**: 清晰描述更改内容
- **描述**: 说明解决的问题、新增功能等
- **测试计划**: 描述如何测试你的更改

### 3. PR 审核

- 等待维护者审核
- 根据反馈进行修改
- 保持 PR 专注于单一功能

## 测试

### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_brightness.py
```

### 编写测试

```python
def test_brightness_control():
    """测试亮度控制功能"""
    brightness = get_brightness()
    assert 0 <= brightness <= 100
```

## 反馈与问题

### 报告 Bug

请包含以下信息：

1. 使用的分支和版本
2. 操作系统和环境
3. 复现步骤
4. 期望行为 vs 实际行为
5. 错误日志或截图

### 功能请求

请包含：

1. 解决的问题或需求
2. 建议的解决方案
3. 任何相关的参考实现

## 行为准则

- 尊重其他贡献者
- 使用友好的语言
- 接受建设性的批评
- 关注社区利益

## 许可证

通过贡献代码，你同意你的代码将按照项目的 [MIT 许可证](https://opensource.org/licenses/MIT) 发布。
