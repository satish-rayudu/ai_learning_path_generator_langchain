from backend import generate_learning_path


result = generate_learning_path(
    topic="Python",
    level="Beginner",
    goal="Become job ready",
    duration="8 weeks",
    hours_per_week=10
)


print("TITLE:")
print(result.title)

print("\nOVERVIEW:")
print(result.overview)

print("\nFINAL PROJECT:")
print(result.final_project)