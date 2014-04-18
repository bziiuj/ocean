name := "mantis_shrimp"

version := "1.0"

scalaVersion := "2.10.2"

resolvers += "Typesafe Repository" at "http://repo.typesafe.com/typesafe/releases/"

libraryDependencies += "com.typesafe.akka" % "akka-actor_2.10" % "2.2-M1"

libraryDependencies += "com.typesafe.akka" % "akka-actor_2.10" % "2.2-M1" classifier "javadoc"

libraryDependencies ++= Seq("com.propensive" %% "rapture-core" % "0.9.0")

libraryDependencies ++= Seq("com.propensive" %% "rapture-json" % "0.9.1")

libraryDependencies ++= Seq("com.propensive" %% "rapture-io" % "0.9.1")

libraryDependencies ++= Seq("com.propensive" %% "rapture-io" % "0.9.1" classifier "javadoc")