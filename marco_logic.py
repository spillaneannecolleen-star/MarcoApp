import datetime

class UserSystem:
    def __init__(self):
        self.user_data = {
            "Current User": {
                "points": 0,
                "level": "Parking Rookie",
                "streak": 5,
                "history": [],
                "reputation": 100  # New: Trust Score
            }
        }
        self.community_total = 750
        self.community_goal = 1000
        self.others = [
            {"name": "Brenda", "points": 450, "reputation": 98, "badges": "🥇🏆"},
            {"name": "Milo_James_Dad", "points": 100, "reputation": 100, "badges": "🥈"}
        ]

    def add_points(self, amount, spot_name):
        user = self.user_data["Current User"]
        user["points"] += amount
        self.community_total += 1
        user["history"].insert(0, f"Reported {spot_name}")
        return user["points"], None

    def report_false_spot(self, spot_owner):
        # In a real app, this would penalize the person who posted the spot
        notification = f"⚠️ Report filed. We're investigating {spot_owner}'s post."
        return notification

    def get_leaderboard(self):
        user = self.user_data["Current User"]
        me = {
            "Name": "You",
            "Points": user["points"],
            "Trust Score": f"{user['reputation']}%",
            "Badges": self.get_badges(user["points"])
        }
        # Simplified leaderboard columns for the Play Store look
        all_players = [me] + [{"Name": o["name"], "Points": o["points"], "Trust Score": f"{o['reputation']}%", "Badges": o["badges"]} for o in self.others]
        return sorted(all_players, key=lambda x: x['Points'], reverse=True)

    def get_badges(self, points):
        badges = ""
        if points >= 50: badges += "🥉"
        if points >= 150: badges += "🥈"
        return badges

class SpotSeeker:
    def __init__(self):
        self.available_spots = [
            {'name': 'Level 1A', 'time': 2, 'lat': 28.5383, 'lon': -81.3792, 'posted_by': 'Brenda'},
            {'name': 'Level 2B', 'time': 5, 'lat': 28.5390, 'lon': -81.3800, 'posted_by': 'ParkingPro_99'}
        ]
    def search_spots(self, query):
        if not query: return self.available_spots
        return [s for s in self.available_spots if query.lower() in s['name'].lower()]

 
