package data.repositories;

import data.models.Guest;

import java.util.ArrayList;
import java.util.List;

public class GuestRepositoryImpl implements GuestRepository {

    private List<Guest> guests = new ArrayList<>();
    private int idCounter = 1;

public Guest save(Guest guest) {
    if (guest.getId() == 0)   {
        guest.setId(idCounter++);
        guests.add(guest);
    }
   return guest;
}

public Guest findById(int id) {
    for (Guest guest : guests) {

        if(guest.getId() == id)     {
            return guest;
        }
    }
    return null;
}

public void deleteById(int id) {
    for (Guest guest : guests) {
        if(guest.getId() == id)     {
            guests.remove(guest);
            break;
        }
    }
}

public int count() {
    return guests.size();
}
}
