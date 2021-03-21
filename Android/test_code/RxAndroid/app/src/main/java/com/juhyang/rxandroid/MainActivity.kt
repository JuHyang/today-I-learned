package com.juhyang.rxandroid

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.juhyang.rxandroid.client.GithubClient
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.schedulers.Schedulers

/*https://leveloper.tistory.com/165*/

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        GithubClient.getApi().getRepos("juhyang")
            .subscribeOn(Schedulers.io())
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe({ items ->
                items.forEach { println(it) }
            }, { e ->
                println (e.toString())
            })
    }
}
