"""
In-memory cache for task tracking
"""

from typing import Dict, Optional, Any
import json

class TaskCache:
    """Asynchronous task cache"""
    
    _instance = None
    _cache: Dict[str, Any] = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TaskCache, cls).__new__(cls)
        return cls._instance
    
    def set_task(self, task_id: str, data: Dict[str, Any]):
        """Task ma'lumotlarini cache-ga saqlash"""
        if task_id not in self._cache:
            self._cache[task_id] = {}
        self._cache[task_id].update(data)
    
    def get_task(self, task_id: str) -> Optional[Dict[str, Any]]:
        """Task ma'lumotlarini cache-dan olish"""
        return self._cache.get(task_id)
    
    def delete_task(self, task_id: str):
        """Task-ni cache-dan o'chirish"""
        if task_id in self._cache:
            del self._cache[task_id]
    
    def get_all_tasks(self) -> Dict[str, Any]:
        """Barcha task-larni olish"""
        return self._cache.copy()
    
    def clear(self):
        """Cache-ni tozalash"""
        self._cache.clear()
