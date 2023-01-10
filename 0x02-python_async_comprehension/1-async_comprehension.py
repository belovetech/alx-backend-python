#!/usr/bin/env python3
"""Async Comprehensions"""


from typing import Generator


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """collect 10 random numbers using an async comprehension
        over async_generator"""
    return [i async for i in async_generator()]
