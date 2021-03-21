package com.juhyang.rxandroid.model

import com.google.gson.annotations.SerializedName

/**

 * Created by juhyang on 3/21/21.

 */
data class GithubRepo (
    @SerializedName("name") val name : String,
    @SerializedName("id") val id : String,
    @SerializedName("created_at") val date : String,
    @SerializedName("html_url") val url : String
)

// @SerializedName 은 Annotation value에 해당하는 데이터를 변수에 바인딩합니다.
