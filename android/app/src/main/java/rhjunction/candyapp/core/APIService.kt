package rhjunction.candyapp.core

import com.jakewharton.retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory
import io.reactivex.Completable
import io.reactivex.Observable
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.GET
import retrofit2.http.Path

interface ApiService {

    @GET("gotobasket/{num}")
    fun goToBasket(@Path("num") basketNumber: Int) : Call<Void>

    @GET("getcandies")
    fun getCandies() : Call<Void>

    @GET("abortcandies")
    fun abortCandies() : Call<Void>

    @GET("fakecandies")
    fun fakeCandies() : Call<Void>

    @GET("goodbye")
    fun goodbye() : Call<Void>

    companion object {
        const val BACKEND_URL = "http://russianhackers228.serveo.net/"

        fun create(): ApiService {
            val retrofit = Retrofit.Builder()
//                .addConverterFactory(GsonConverterFactory.create())
                .addCallAdapterFactory(RxJava2CallAdapterFactory.create())
                .baseUrl(BACKEND_URL)
                .build()

            return retrofit.create(ApiService::class.java)
        }

        fun callWithNext(number: Int, calls: MutableList<Call<Void>>) {
            if (number < calls.size) {
                calls[number].enqueue(object : Callback<Void> {
                    override fun onResponse(call: Call<Void>, response: Response<Void>) {
                        Thread.sleep(10 * 1000)
                        callWithNext(number + 1, calls)
                    }

                    override fun onFailure(call: Call<Void>, t: Throwable) {
                    }

                })
            }
        }
    }

}