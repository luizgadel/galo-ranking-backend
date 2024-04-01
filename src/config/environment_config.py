from dotenv import load_dotenv

class Environment:
    
    def config_environment(env):
        config_type = env
        match config_type:
            case 'localhost':
                load_dotenv(".env.localhost")