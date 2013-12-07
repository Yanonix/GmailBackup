#!/usr/bin/python
# -*- coding: utf-8 -*-
import imaplib
import os
import sys

# Private centralization of notification
try:
    import maya
except ImportError:
    pass

class GmailBackup():
    def __init__(self, l, p, backup_dir):
        self.l = l
        self.p = p
        self.backup_dir = backup_dir

    def connect(self):
        self.m = imaplib.IMAP4_SSL("imap.gmail.com")
        try:
            self.m.login(self.l, self.p)
        except :
            print >> sys.stderr, "Something wrong ? Bad logins ?"
            exit()

        # Sélection du dossier
        # print self.m.list("All")

        if(self.m.select("[Gmail]/Tous les messages", readonly=True)[0] == 'NO'):
            self.m.select("[Gmail]/All Mail", readonly=True)

    def save(self, search='ALL'):
        # Recherche de tous les messages
        #_, items = self.m.search(None, search)  # ALL # (HEADER Subject "Yanonix")
        _, items = self.m.uid('search', None, 'ALL')
        l = items[0]
        items = l.split()
        count = len(items)
        i = 1
        nb_new = 0
        print("Mails quantity : %d" % count)

        for mid in items:

            name = "%s/%s.mail" % (self.backup_dir, mid)
            print("(%d%%) N°%d\t UID°%s" % (i*100/count, i, mid)),

            if not os.path.isfile(name):
                print(" ! New !")
                try:
                    resp, data = self.m.fetch('%d' % (i), "(RFC822)")
                    body = data[0][1]

                    f = open(name, "a")
                    f.write(body)
                    f.close()
                    nb_new += 1

                except (KeyboardInterrupt, SystemExit):
                    if os.path.isfile(name):
                        os.remove(name)
                        print("\n\tFile %s deleted" % name)
                    exit()
                    
                except (TypeError):
                    print("\tType error")
                    if maya:
                        maya.fatal("Gmail", "download", "type", "Erreur de type lors d'un téléchargement")

                print("\n"),
            else:
                print("\r"),

            i += 1

        if nb_new > 0:
            print("%d new mails saved" % nb_new)
            if maya:
                maya.success("Gmail", "new", nb_new, "%d nouveaux mails récupérés" % nb_new)




try:
    from __configuration__ import username, password, directory
    print("GmailBackup (from __configuration__.py)\nConnection...")
    GB = GmailBackup(username, password, directory)

except ImportError:
    import argparse
    print("GmailBackup (from command line)")
    parser = argparse.ArgumentParser(description='Gmail backup system')
    parser.add_argument('username', type=str, help='username@gmail.com')
    parser.add_argument('password', type=str, help='Password for connection')
    parser.add_argument('directory', type=str, help='Directory for emails backup')

    args = parser.parse_args()

    print("Connection...")
    GB = GmailBackup(args.username, args.password, args.directory)


GB.connect()
print("Backup...")
GB.save()
