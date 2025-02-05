from fastapi import FastAPI
from graphql import GraphQLSchema, GraphQLObjectType, GraphQLField, GraphQLString
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp

app = FastAPI()

# Define GraphQL schema
schema = GraphQLSchema(
    query=GraphQLObjectType(
        name="Query",
        fields={
            "hello": GraphQLField(
                type=GraphQLString,
                resolver=lambda obj, info: "Hello, world!"
            )
        }
    )
)

# Add GraphQL endpoint
app.add_route("/graphql", GraphQLApp(schema=schema, executor_class=AsyncioExecutor))
