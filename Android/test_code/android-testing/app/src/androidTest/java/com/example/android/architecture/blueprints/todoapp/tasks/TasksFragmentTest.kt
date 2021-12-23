package com.example.android.architecture.blueprints.todoapp.tasks

import android.content.Context
import android.os.Bundle
import androidx.fragment.app.testing.launchFragmentInContainer
import androidx.navigation.NavController
import androidx.navigation.Navigation
import androidx.recyclerview.widget.RecyclerView
import androidx.test.core.app.ApplicationProvider.getApplicationContext
import androidx.test.espresso.Espresso.onView
import androidx.test.espresso.action.ViewActions.click
import androidx.test.espresso.assertion.ViewAssertions
import androidx.test.espresso.contrib.RecyclerViewActions
import androidx.test.espresso.matcher.ViewMatchers.*
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.filters.MediumTest
import com.example.android.architecture.blueprints.todoapp.FakeAndroidTestRepository
import com.example.android.architecture.blueprints.todoapp.R
import com.example.android.architecture.blueprints.todoapp.ServiceLocator
import com.example.android.architecture.blueprints.todoapp.data.Task
import com.example.android.architecture.blueprints.todoapp.data.source.TasksRepository
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.test.runBlockingTest
import org.junit.After
import org.junit.Before
import org.junit.Test
import org.junit.runner.RunWith
import org.mockito.Mockito.mock
import org.mockito.Mockito.verify

/*
* Created by Juhyang on 2021/12/23
*/

@MediumTest // 테스트를 "중간 런타임" 통합 테스트로 표시합니다 (@Small 단위 테스트 및 @LargeTest 종단 간 테스트 대비). 이렇게 하면 실행할 테스트 크기를 그룹화 하고 선택하는 데 도움이 됩니다.
@RunWith(AndroidJUnit4::class) // AndroidX 테스트를 사용하는 모든 클래스에서 사용됩니다.
@ExperimentalCoroutinesApi
class TasksFragmentTest {

    private lateinit var repository: TasksRepository

    @Before
    fun initRepository() {
        repository = FakeAndroidTestRepository()
        ServiceLocator.tasksRepository = repository
    }

    @After
    fun cleanupDb() = runBlockingTest {
        ServiceLocator.resetRepository()
    }

    @Test
    fun clickTask_navigateToDetailFragmentOne() = runBlockingTest {
        repository.saveTask(Task("TITLE1", "DESCRIPTION1", false, "id1"))
        repository.saveTask(Task("TITLE2", "DESCRIPTION2", true, "id2"))

        // GIVEN - On the home screen
        val scenario = launchFragmentInContainer<TasksFragment>(Bundle(), R.style.AppTheme)

        val navController = mock(NavController::class.java)
        scenario.onFragment {
            Navigation.setViewNavController(it.view!!, navController)
        }

        // WHEN - Click on the first list item
        onView(withId(R.id.tasks_list))
            .perform(
                RecyclerViewActions.actionOnItem<RecyclerView.ViewHolder>(
                    hasDescendant(withText("TITLE1")), click()
                )
            )


        // THEN - Verify that we navigate to the first detail screen
        verify(navController).navigate(
            TasksFragmentDirections.actionTasksFragmentToTaskDetailFragment("id1")
        )
    }

    @Test
    fun clickAddTaskButton_navigateToAddEditFragment()  {
        // GIVEN - On the home screen
        val scenario = launchFragmentInContainer<TasksFragment>(Bundle(), R.style.AppTheme)

        val navController = mock(NavController::class.java)
        scenario.onFragment {
            Navigation.setViewNavController(it.view!!, navController)
        }

        onView(withId(R.id.edit_task_fab)).perform(click())

        verify(
            navController.navigate(
                TasksFragmentDirections.actionTasksFragmentToAddEditTaskFragment(
                    null,
                    getApplicationContext<Context>().getString(R.string.add_task)
                )
            )
        )
    }
}