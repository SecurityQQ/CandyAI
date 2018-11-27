package rhjunction.candyapp.main

import Storage
import android.content.Intent
import android.opengl.Visibility
import android.os.Bundle
import android.support.design.widget.BottomNavigationView
import android.support.v7.app.AppCompatActivity
import android.support.v7.widget.LinearLayoutManager
import android.view.View
import at.anchor.game.CallbackAPI
import kotlinx.android.synthetic.main.activity_main.*
import rhjunction.candyapp.R
import rhjunction.candyapp.core.ApiService
import rhjunction.candyapp.game.AndroidLauncher
import rhjunction.candyapp.game.GameHandler


class MainActivity : AppCompatActivity() {

    val apiService = ApiService.create()
    lateinit var callbackListener: CallbackListener

    private val mOnNavigationItemSelectedListener = BottomNavigationView.OnNavigationItemSelectedListener { item ->
        when (item.itemId) {
            R.id.navigation_home -> {
                return@OnNavigationItemSelectedListener true
            }
            R.id.navigation_dashboard -> {
                if (Storage.getLives() > 0) {
                    intent = Intent(this, AndroidLauncher::class.java)
                    startActivity(intent)
                } else {

                }
                return@OnNavigationItemSelectedListener true
            }
            R.id.navigation_notifications -> {
                return@OnNavigationItemSelectedListener true
            }
        }
        false
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

//        navigation.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener)

        callbackListener = CallbackListener(apiService)
        Model.callbackListener = callbackListener
        Storage.init(this)
        GameHandler.init(apiService)

        initContent()
    }

    private fun initContent() {
        games_rv.layoutManager = LinearLayoutManager(this)
        games_rv.adapter = GameAdapter(this)
        games_rv.setHasFixedSize(true)

        scoreView.text = Storage.getProgress().toString()
        when (GameHandler.lives) {
            2 -> {
                heart_3.visibility = View.GONE
                heart_1.visibility = View.VISIBLE
                heart_2.visibility = View.VISIBLE
            }
            1 -> {
                heart_3.visibility = View.GONE
                heart_2.visibility = View.GONE
                heart_1.visibility = View.VISIBLE
            }
            0 -> {
                heart_3.visibility = View.GONE
                heart_2.visibility = View.GONE
                heart_1.visibility = View.GONE
            }
            else -> {}
        }
        checkpoint.text = GameHandler.getCheckpointNumber().toString()
    }

    override fun onResume() {
        super.onResume()
        initContent()
        if (GameHandler.isInit()) {
            GameHandler.decideOnAward()
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        if (GameHandler.isInit()) {
            GameHandler.sayGoodbye()
        }
    }

    inner class CallbackListener(apiService: ApiService) : CallbackAPI {

        val context = this@MainActivity

        init {
            Storage.init(context)
            GameHandler.init(apiService)
        }

        override fun onBackPressed() {

        }

        override fun submitResult(user: String?, score: Int) {
            if (score > 0) {
                Storage.addProgress(score)
            }
            Storage.deleteLife()
        }

    }
}
