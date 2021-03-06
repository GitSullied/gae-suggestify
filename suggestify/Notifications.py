import suggestify

class NotificationsHandler (suggestify.Request) :

    def get (self) :

        if not self.check_logged_in(self.min_perms) :
            self.do_flickr_auth(self.min_perms)
            return
        
        self.display("notifications.html")
        return
