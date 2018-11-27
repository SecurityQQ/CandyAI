package rhjunction.candyapp.game

import android.annotation.SuppressLint
import android.telecom.Call
import android.util.Log
import android.widget.Toast
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.schedulers.Schedulers
import retrofit2.Callback
import retrofit2.Response
import rhjunction.candyapp.core.ApiService
import rhjunction.candyapp.main.random

object GameHandler {

    val checkpoints = mutableListOf(100, 300, 600)
    var awardsReceived = mutableListOf(false, false, false)
    val maxProgress = 1000

    lateinit var apiService: ApiService
    val progress: Int
        get() = Storage.getProgress()
    val lives: Int
        get() = Storage.getLives()

    fun init(service: ApiService) {
        apiService = service
    }

    fun isInit() : Boolean = ::apiService.isInitialized

    fun getCheckpointNumber() : Int {
        var checkpointNumber = 0
        for (point in checkpoints) {
            if (progress >= point) {
                checkpointNumber += 1
            }
        }
        return checkpointNumber
    }

    fun getProgressPercentage() : Float = progress.toFloat() / maxProgress * 100

    @SuppressLint("CheckResult")
    fun decideOnAward() {
        val checkpoint = getCheckpointNumber()
        val storageCheckpoint = Storage.getCheckpointNumber()
        if (storageCheckpoint == checkpoint) {
            return
        }
        if (checkpoint == 1) {
            val basket = (0..3).random()

            ApiService.callWithNext(0, mutableListOf(apiService.goToBasket(basket),
                apiService.fakeCandies(),
                apiService.goodbye(),
                apiService.getCandies(),
                apiService.abortCandies()))

            Storage.saveCheckpointNumber(checkpoint)
        } else if (checkpoint > 1) {
            val basket = (0..3).random()

            ApiService.callWithNext(0, mutableListOf(apiService.goToBasket(basket),
                                                             apiService.getCandies(),
                                                             apiService.abortCandies()))

            Storage.saveCheckpointNumber(checkpoint)
        }
    }

    @SuppressLint("CheckResult")
    fun sayGoodbye() {
        apiService.goodbye().enqueue(object : Callback<Void> {
            override fun onResponse(call: retrofit2.Call<Void>, response: Response<Void>) {

            }

            override fun onFailure(call: retrofit2.Call<Void>, t: Throwable) {

            }

        })
    }

}
