package com.example.android.architecture.blueprints.todoapp

import android.content.Context
import androidx.annotation.VisibleForTesting
import androidx.room.Room
import com.example.android.architecture.blueprints.todoapp.data.source.DefaultTasksRepository
import com.example.android.architecture.blueprints.todoapp.data.source.TasksRepository
import com.example.android.architecture.blueprints.todoapp.data.source.local.TasksLocalDataSource
import com.example.android.architecture.blueprints.todoapp.data.source.local.ToDoDatabase
import com.example.android.architecture.blueprints.todoapp.data.source.remote.TasksRemoteDataSource
import kotlinx.coroutines.runBlocking

/*
* Created by Juhyang on 2021/12/23
*/

object ServiceLocator {

    private var database: ToDoDatabase? = null

    private val lock = Any()

    @Volatile
    var tasksRepository: TasksRepository? = null
        @VisibleForTesting set

    @VisibleForTesting
    fun resetRepository() {
        synchronized(lock) {
            runBlocking { TasksRemoteDataSource.deleteAllTasks() }
        }
        // Clear all data to avoid test pollution
        database?.apply {
            clearAllTables()
            close()
        }
        database = null
        tasksRepository = null
    }

    fun provideTasksRepository(context: Context): TasksRepository {
        synchronized(this) {
            return tasksRepository ?: createTaskRepository(context)
        }
    }

    private fun createTaskRepository(context: Context): TasksRepository {
        val newRepo =
            DefaultTasksRepository(TasksRemoteDataSource, createTaskLocalDataSource(context))
        tasksRepository = newRepo
        return newRepo
    }

    private fun createTaskLocalDataSource(context: Context): TasksLocalDataSource {
        val database = database ?: createDatabase(context)
        return TasksLocalDataSource(database.taskDao())
    }

    private fun createDatabase(context: Context): ToDoDatabase {
        val result =
            Room.databaseBuilder(context.applicationContext, ToDoDatabase::class.java, "Tasks.db")
                .build()
        database = result
        return result
    }
}