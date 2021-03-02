package com.example.snaprecyclerview

import android.content.res.Resources
import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearSnapHelper
import androidx.recyclerview.widget.RecyclerView
import androidx.recyclerview.widget.SnapHelper
import com.azoft.carousellayoutmanager.CarouselLayoutManager
import com.azoft.carousellayoutmanager.CarouselZoomPostLayoutListener
import com.azoft.carousellayoutmanager.CenterScrollListener

class MainActivity : AppCompatActivity() {
    lateinit var recyclerView : RecyclerView
    var snapHelper = LinearSnapHelper()
    var layoutManager = CarouselLayoutManager(CarouselLayoutManager.HORIZONTAL, false)

    private var indexOfFrontChild = 2

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val list = ArrayList<String>()
        for (i in 0 until 10) {
            list.add(i.toString())
        }

        this.layoutManager.setPostLayoutListener(CarouselZoomPostLayoutListener())

        val adapter = RecyclerAdapter(list)
        this.recyclerView = findViewById(R.id.main_recyclerView)
        this.recyclerView.adapter = adapter
        this.recyclerView.setHasFixedSize(true)
        this.recyclerView.layoutManager = this.layoutManager
        this.recyclerView.addOnScrollListener(CenterScrollListener())
    }

    private fun getCurrentItem(): Int = snapHelper.getSnapPosition(this.recyclerView)

    fun SnapHelper.getSnapPosition(recyclerView : RecyclerView) : Int {
        val layoutManager = recyclerView.layoutManager ?: return RecyclerView.NO_POSITION
        val snapView = findSnapView(layoutManager) ?: return RecyclerView.NO_POSITION
        return layoutManager.getPosition(snapView)
    }
}
