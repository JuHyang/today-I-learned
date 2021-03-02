package com.example.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.util.Log
import android.view.View
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import java.util.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        GlobalScope.launch(Dispatchers.Main) {
            while (true) {
                delay(1)
                val temp = "12312312312312"
                Log.d("hyang@temp", "${temp}")
                Log.d("hyang@GlobalScope", "${"GlobalScope"}")
                Handler(Looper.getMainLooper()).postDelayed({
                    Log.d("hyang@Handler", "${"Handler"}")
                }, 1)
            }
        }

        Timer().schedule(object : TimerTask() {
            override fun run() {
                Log.d("hyang@1", "${11}")
                return
            }

        }, 1, 1)
    }
}