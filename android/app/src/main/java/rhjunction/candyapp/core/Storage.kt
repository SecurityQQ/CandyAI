import android.content.Context
import android.content.SharedPreferences

object Storage {

    const val PROGRESS_KEY = "progress"
    const val LIFE_KEY = "lives"
    const val DEFAULT_LIVES = 3

    lateinit var prefs: SharedPreferences

    fun init(context: Context) {
        prefs = context.getSharedPreferences("main_prefs", Context.MODE_PRIVATE)
        initLives()
    }

    private fun writeInt(key: String, value: Int) {
        val editor = prefs.edit()
        editor.putInt(key, value)
        editor.apply()
    }

    private fun getInt(key: String) : Int? {
        val value = prefs.getInt(key, -1)
        return if (value != -1) {
            value
        } else {
            null
        }
    }

    fun addProgress(score: Int) {
        var progress = getProgress()
        progress += score
        writeInt(PROGRESS_KEY, progress)
    }

    fun getProgress() : Int = getInt(PROGRESS_KEY) ?: 0

    fun initLives() {
        if (getInt(LIFE_KEY) == null)
            writeInt(LIFE_KEY, DEFAULT_LIVES)
    }

    fun getLives() : Int = getInt(LIFE_KEY) ?: DEFAULT_LIVES

    fun deleteLife() {
        val lives = getLives()
        writeInt(LIFE_KEY, lives - 1)
    }

    fun addLives(n: Int) {
        val lives = getLives()
        writeInt(LIFE_KEY, lives + n)
    }

//    fun saveAwards(awards: MutableList<Boolean>) {
//        awards.forEachIndexed { index, bool ->
//            if (bool) {
//                writeInt("check{$index}", 1)
//            } else {
//                writeInt("check{$index}", 0)
//            }
//        }
//    }
//
//    fun loadAwards() : MutableList<Boolean> {
//        val awards = mutableListOf<Boolean>()
//        awards.add(0, getInt("check0") == 1)
//        awards.add(1, getInt("check1") == 1)
//        awards.add(2, getInt("check2") == 1)
//        return awards
//    }

    fun saveCheckpointNumber(num: Int) {
        writeInt("checkNumber", num)
    }

    fun getCheckpointNumber() = getInt("checkNumber") ?: 0

}