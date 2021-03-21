package com.juhyang.rxandroid.service

import com.juhyang.rxandroid.model.GithubRepo
import io.reactivex.Single
import retrofit2.http.GET
import retrofit2.http.Path

/**

 * Created by juhyang on 3/21/21.

 */
interface GithubService {
    @GET("users/{owner}/repos")
    fun getRepos(@Path("owner") owner : String) : Single<List<GithubRepo>>
}
