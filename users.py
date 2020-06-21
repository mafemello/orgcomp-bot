class Users():
    def __init__(self):
        self.all_users = {}

    def create_user(self, user_id):
        user_id = str(user_id)
        if not user_id in self.all_users:
            self.all_users.update(
                    {
                        f'{user_id}':{
                            'id': user_id,
                            'acertos_quizz_assembly': 0,
                            'acertos_quizz_datapass': 0,
                            'acertos_quizz_cache': 0,
                        }
                    }
                )
            
            return True
        return False
