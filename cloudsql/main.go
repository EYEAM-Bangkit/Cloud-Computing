package main

import (
	"database/sql"
	"fmt"
	"log"
	"net/http"
	"os"
)

func main() {

	dbPool, err := initTCPConnectionPool()
	if err != nil {
		log.Fatal(err)
	}

	http.HandleFunc("/", handler(dbPool))

	log.Fatal(http.ListenAndServe(":8080", nil))
}

func handler(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		err := db.Ping()
		if err != nil {
			log.Println(err)
			w.WriteHeader(http.StatusInternalServerError)
			w.Write([]byte("error while trying to connect to database"))
			return
		}

		w.WriteHeader(http.StatusOK)
		w.Write([]byte("ping success to database"))
		log.Println("ping success")
	}
}

func initTCPConnectionPool() (*sql.DB, error) {
	// [START cloud_sql_postgres_databasesql_create_tcp]
	var (
		dbUser    = os.Getenv("my-db-user")     // e.g. 'my-db-user'
		dbPwd     = os.Getenv("my-db-password") // e.g. 'my-db-password'
		dbTCPHost = os.Getenv("127.0.0.1")  	// e.g. '127.0.0.1' ('172.17.0.1' if deployed to GAE Flex)
		dbPort    = "5432"                 		// e.g. '5432'
		dbName    = os.Getenv("my-db-name") 	// e.g. 'my-db-name'
	)

	var dbURI string
	dbURI = fmt.Sprintf("host=%s user=%s password=%s port=%s database=%s", dbTCPHost, dbUser, dbPwd, dbPort, dbName)

	// dbPool is the pool of database connections.
	dbPool, err := sql.Open("mysql", dbURI)
	if err != nil {
		return nil, fmt.Errorf("sql.Open: %v", err)
	}

	// ...

	return dbPool, nil
}
