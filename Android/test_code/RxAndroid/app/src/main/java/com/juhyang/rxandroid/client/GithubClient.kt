package com.juhyang.rxandroid.client

import com.juhyang.rxandroid.service.GithubService
import okhttp3.OkHttpClient
import retrofit2.Retrofit
import retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory
import retrofit2.converter.gson.GsonConverterFactory

/**

 * Created by juhyang on 3/21/21.

 */
object GithubClient {
    const val BASE_URL = "https://api.github.com"

    fun getApi(): GithubService = Retrofit.Builder()
        .baseUrl(BASE_URL)
        .client(OkHttpClient())
        .addCallAdapterFactory(RxJava2CallAdapterFactory.create()) // 기존의 Retrofit Call 이라는 Response Type을 Rx의 Single 또는 Observable로 변환하기 위해서다.
        .addConverterFactory(GsonConverterFactory.create()) // Json 의 형태로 전달 받는 Response를 사용자가 정의해놓은 인자들에 매칭시키기 위한 Converter이다.
        .build()
        .create(GithubService::class.java)
}
