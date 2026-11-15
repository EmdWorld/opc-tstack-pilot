# TASK：为 math_utils 增加 is_prime + 测试，然后走 full-stop 流水线

## 任务

1. 在 `src/math_utils.py` 中新增函数 `is_prime(n)`：
   - 输入整数 n，返回布尔值
   - n < 2 返回 False；用试除法（除到 sqrt(n)）判断
2. 在 `tests/test_math_utils.py` 中新增对应测试（至少覆盖：2 是素数、1 不是、负数、9 不是、97 是、100 不是）
3. 本地跑 `python3 -m pytest tests/ -q` 确保全绿（含既有测试）

## 完成后：走 full-stop 交付流水线（按技能库的 full-stop 技能执行）

- 证明改动有效（测试通过）
- 开一个以"问题优先"的 PR（按 file-pr 技能的格式）
- PR 就绪后**停下**——绝不合并，等人工在 GitHub 页面点合并
- PR 描述里写清：做了什么、测试证据、留给人的检查点
