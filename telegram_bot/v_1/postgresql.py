import postgres as pst


async def db_start():
    global db, cur

    db = pst.connect('new_db')
    cur = db.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, key_word TEXT, product_card TEXT, buy_back_amount INTEGER)"
    )

    db.commit()


async def create_rofile(user_id):
    user = cur.execute(
        "SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)
    ).fetchone()
    if not user:
        cur.execute(
            "INSERT INTO profile VALUES(?, ?, ?, ?)", (user_id, '', '', '')
        )
        db.commit()

async def edit_profile(state, user_id):
    async with state.proxy() as data:
        cur.execute(
            "UPDATE profile WHERE user_id == '{}' SET key_word = '{}', SET product_card = '{}', SET buy_back_amount = '{}' ".format(
            user_id, data['key_word'], data['product_card'], data['buy_back_amount'])
        )
        db.commit()
