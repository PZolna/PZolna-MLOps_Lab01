from settings import Settings


def test_settings_are_loaded_from_test_environment():
    settings = Settings()

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "ml-api-test"
    assert settings.API_KEY == "test-api-key"
