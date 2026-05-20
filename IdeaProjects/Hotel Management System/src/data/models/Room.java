package data.models;

public class Room {
    private int id;
    private int roomNumber;
    private RoomType roomType;
    private double prices;
    private boolean isAvailable;

    public Room (double prices, boolean isAvailable, int roomNumber)    {
        this.roomNumber = roomNumber;
        this.prices = prices;
        this.isAvailable = isAvailable;

    }




}