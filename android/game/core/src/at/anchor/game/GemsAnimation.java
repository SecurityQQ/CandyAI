package at.anchor.game;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.assets.AssetManager;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.g2d.TextureAtlas;
import com.badlogic.gdx.graphics.g2d.TextureRegion;

public class GemsAnimation {

    private EsthetiqueGems _game;
    private TextureRegion[] _imgGems;
    private TextureAtlas _atlasGems;
    private int[] _posX;
    private int _posY;

    double _animTime;
    double _animTotalTime;

    public GemsAnimation(EsthetiqueGems esthetiqueGems) {
        _game = esthetiqueGems;

        AssetManager assetManager = _game.getAssetManager();

        _imgGems = new TextureRegion[7];
        _posX = new int[7];

        _imgGems[0] = new TextureRegion(_game.getAtlasGems().findRegion("1"));
        _imgGems[1] = new TextureRegion(_game.getAtlasGems().findRegion("2"));
        _imgGems[2] = new TextureRegion(_game.getAtlasGems().findRegion("3"));
        _imgGems[3] = new TextureRegion(_game.getAtlasGems().findRegion("4"));
        _imgGems[4] = new TextureRegion(_game.getAtlasGems().findRegion("5"));
        _imgGems[5] = new TextureRegion(_game.getAtlasGems().findRegion("6"));
        _imgGems[6] = new TextureRegion(_game.getAtlasGems().findRegion("7"));


        for (int i = 0; i < 7; ++i) {
            _imgGems[i].flip(false, true);
            _posX[i] = EsthetiqueGems.VIRTUAL_WIDTH - 360 - (76 * 7) / 2 + i * 76;
        }

        _posY = 432;

        _animTime = 0.0;
        _animTotalTime = 0.5;
    }

    public void draw(double deltaT) {
        if(_animTime < 7 * 5 + _animTotalTime)
            _animTime += deltaT;

        SpriteBatch batch = _game.getSpriteBatch();

        for(int i = 0; i < 7; ++i) {
            double composedTime = _animTime - i * _animTotalTime / 7.0f;
            if (composedTime < 0) {
                continue;
            }

            if (composedTime < _animTotalTime) {
                batch.draw(_imgGems[i], _posX[i], Animation.easeOutCubic((float)composedTime, 600.0f, (float)_posY - 600.0f, _animTotalTime));
            }else{
                batch.draw(_imgGems[i], _posX[i], _posY);
            }
        }
    }
}

