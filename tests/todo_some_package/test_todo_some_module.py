# -*- coding: utf-8 -*-

import todo_some_package.todo_some_module


def test_answer() -> None:
    assert todo_some_package.todo_some_module._some_func() == 'test'
