package rhjunction.candyapp.main

import android.content.Context
import android.content.Intent
import android.graphics.BitmapFactory
import android.support.v4.graphics.drawable.RoundedBitmapDrawableFactory
import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import rhjunction.candyapp.R
import rhjunction.candyapp.game.AndroidLauncher

class GameAdapter(val context: Context) : RecyclerView.Adapter<GameAdapter.ViewHolder>() {
    val data = sampleGames

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        with(holder) {
            name.text = data[position].name

            val resID = context.resources.getIdentifier(data[position].imageResName,
                        "drawable", context.packageName)
            val bitmap = BitmapFactory.decodeResource(context.resources, resID)
            val roundedDrawable = RoundedBitmapDrawableFactory.create(context.resources, bitmap)
            roundedDrawable.cornerRadius = 20f

            image.setImageDrawable(roundedDrawable)

            if (position == 0) {
                button.setOnClickListener {
                    if (Storage.getLives() > 0) {
                        val intent = Intent(context, AndroidLauncher::class.java)
                        context.startActivity(intent)
                    } else {

                    }
                }
            }
        }
    }

    override fun getItemCount(): Int = sampleGames.size

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val itemView = LayoutInflater.from(parent.context).inflate(R.layout.game_viewholder,
            parent, false)
        return ViewHolder(itemView)
    }

    inner class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        var name: TextView = itemView.findViewById(R.id.name)
        var image: ImageView = itemView.findViewById(R.id.bg_image)
        val button: Button = itemView.findViewById(R.id.button)
    }
}