package rhjunction.candyapp.game;

import android.os.Bundle;

import at.anchor.game.EsthetiqueGems;
import com.badlogic.gdx.backends.android.AndroidApplication;
import com.badlogic.gdx.backends.android.AndroidApplicationConfiguration;
import rhjunction.candyapp.main.Model;

public class AndroidLauncher extends AndroidApplication {


    @Override
    protected void onCreate (Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        AndroidApplicationConfiguration config = new AndroidApplicationConfiguration();

        config.useGL30 = false;
        config.useImmersiveMode = true;

        initialize(new EsthetiqueGems(Model.callbackListener), config);
    }
}
