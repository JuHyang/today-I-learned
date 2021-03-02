package com.example.snaprecyclerview

import android.content.res.Resources
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.core.view.ViewCompat
import androidx.recyclerview.widget.RecyclerView

/**

 * Created by juhyang on 2/26/21.

 */
class RecyclerAdapter(val list : ArrayList<String>) : RecyclerView.Adapter<RecyclerAdapter.CustomViewHolder>() {

    class CustomViewHolder(var view : View) : RecyclerView.ViewHolder(view) {
        val textView : TextView = view.findViewById(R.id.item_text)

        fun bindView(text : String) {
            textView.text = text

            view.setOnFocusChangeListener { v, hasFocus ->
                if (hasFocus) {
                    ViewCompat.setElevation(view, 1f)
                } else {
                    ViewCompat.setElevation(view, 0f)
                }
            }
            
            Log.d("hyang@text", "${text}")
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CustomViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.item, parent, false)
        val width = (Resources.getSystem().displayMetrics.widthPixels * 0.7).toInt()    // 화면 너비의 70%
        view.layoutParams.width = width
        return CustomViewHolder(view)
    }

    override fun onBindViewHolder(holder: CustomViewHolder, position: Int) {
        holder.bindView(list[position])
    }

    override fun getItemCount(): Int {
        return list.size
    }
}
